"""QA Test App v2

  This adds the PIP module to the HR portal.

  Note: This app is intended only for testing and not for any other purpose.
        there are intentional bugs and security issues in this code.
"""

from flask import Flask, render_template, redirect, url_for, request, current_app, flash
from flask_babel import Babel
from peewee import IntegrityError, DoesNotExist
from playhouse.shortcuts import model_to_dict

from model import (
    db,
    EmployeeStatuses,
    Employees,
    Departments,
    Offices,
    OnboardingChecklists,
    Pips,
    PipStatuses,
    PipTaskGrades,
    PipTasks,
)

app = Flask(__name__, static_folder="static", static_url_path="")
app.config[
    "SECRET_KEY"
] = "60fcdad79961a803476b8f4718300892f1e5224c51605178360b3613f117826e"


# Setup Flask-Babel ============================================================
babel = Babel(app, default_locale="en")
AVAILABLE_LOCALES = ["en", "es"]


def get_locale():
    return request.accept_languages.best_match(AVAILABLE_LOCALES)


babel.init_app(app, locale_selector=get_locale)
# ==============================================================================


# Application Routes ===========================================================
@app.route("/")
def index():
    """Site Index"""

    # Local vars
    data = {}

    # Get the list of employees
    data["employees"] = Employees.select()

    # Send them the working template
    return render_template("index.html", data=data)


@app.route("/employee_table")
def employee_table():
    """The Employee Table"""

    # Local vars
    data = {}

    # Get the list of employees
    data["employees"] = Employees.select()

    # Return the loaded template
    return render_template("employee_table.html", data=data)


@app.route("/add_employee")
def add_employee():
    """Display the add employee form"""

    # Local vars
    data = {}

    # We need to pull the employee status, departments, and offices
    data["employee_statuses"] = EmployeeStatuses.select()
    data["departments"] = Departments.select()
    data["offices"] = Offices.select()

    return render_template("add_employee.html", data=data)


@app.route("/employee", methods=["POST"])
def save_employee():
    """Save a new employee record"""

    # Capture the request from the user
    name = request.form.get("name")
    years = request.form.get("years")
    status = request.form.get("status")
    department = request.form.get("department")
    office = request.form.get("office")

    # Let's save the employee in the database
    Employees.create(
        name=name, years=int(years), status=status, office=office, department=department
    )

    # Send them back to the employee table
    return redirect(url_for("employee_table"))


@app.route("/edit_employee/<eid>")
def edit_employee(eid):
    """Display the edit employee form"""

    # Local Vars
    data = {}

    # Get the data for this employee
    employee = Employees.select().where(Employees.id == eid).get()
    data["id"] = employee.id
    data["name"] = employee.name
    data["years"] = employee.years
    data["status"] = employee.status.id
    data["department"] = employee.department.id
    data["office"] = employee.office.id

    # We need to pull the employee status, departments, and offices
    data["employee_statuses"] = EmployeeStatuses.select()
    data["departments"] = Departments.select()
    data["offices"] = Offices.select()

    # Now return the loaded template
    return render_template("edit_employee.html", data=data)


@app.route("/employee/<eid>", methods=["PUT"])
def update_employee(eid):
    """Update an employee record"""

    # Get the values from the user
    name = request.form.get("name")
    years = request.form.get("years")
    status = request.form.get("status")
    department = request.form.get("department")
    office = request.form.get("office")

    # Update the database record
    Employees.update(
        {
            Employees.name: name,
            Employees.years: years,
            Employees.status: status,
            Employees.department: department,
            Employees.office: office,
        }
    ).where(Employees.id == eid).execute()

    return redirect(url_for("employee_table"), 303)


@app.route("/employee/<eid>", methods=["DELETE"])
def delete_employee(eid):
    """Delete an employee"""

    # Delete the requested employee
    Employees.delete().where(Employees.id == eid).execute()

    return redirect(url_for("employee_table"), 303)


@app.route("/offices")
def office_index():
    """Display the list of offices"""

    # local vars
    data = {}

    # Get the list of offices from the database
    data["offices"] = Offices.select()

    # Return the template loaded with the offices
    return render_template("offices.html", data=data)


@app.route("/offices", methods=["POST"])
def add_office():
    """Create a new office"""

    # local vars
    data = {}

    # Create the new office
    Offices.create(name=request.form.get("office_name"))

    # Get the list of offices from the database
    data["offices"] = Offices.select()

    # Return the template loaded with the offices
    return render_template("offices.html", data=data)


@app.route("/edit_office/<oid>")
def edit_office(oid):
    """The edit office form"""

    # Local vars
    data = Offices.select().where(Offices.id == oid).get()

    # Send the edit office form with the selected office loaded
    return render_template("edit_office.html", data=data)


@app.route("/offices/<oid>", methods=["PUT"])
def update_office(oid):
    """The update the office"""

    new_office_name = request.form.get("office_name")

    # Update the office
    Offices.update({Offices.name: new_office_name}).where(Offices.id == oid).execute()

    # Get the new value and send it to the user
    data = Offices.select().where(Offices.id == oid).get()

    # Send the office table row with the selected office loaded
    return render_template("view_office.html", data=data)


@app.route("/offices/<oid>", methods=["DELETE"])
def delete_office(oid):
    """Delete the office"""

    # Delete the office in the database
    try:
        Offices.delete().where(Offices.id == oid).execute()
    except IntegrityError as e:
        return (f"Failed to delete the office: <br>{e}", 500)

    # return them to the updated office list
    return redirect(url_for("office_index"), 303)


@app.route("/departments")
def departments_index():
    """Display the list of departments"""

    # local vars
    data = {}

    # Get the list of departments from the database
    data["departments"] = Departments.select()

    # Return the template loaded with the departments
    return render_template("departments.html", data=data)


@app.route("/departments", methods=["POST"])
def add_department():
    """Create a new department"""

    # local vars
    data = {}

    # Create the new department
    Departments.create(name=request.form.get("department_name"))

    # Get the list of departments from the database
    data["departments"] = Departments.select()

    # Return the template loaded with the departments
    return render_template("departments.html", data=data)


@app.route("/edit_department/<oid>")
def edit_department(oid):
    """The edit department form"""

    # Local vars
    data = Departments.select().where(Departments.id == oid).get()

    # Send the edit department form with the selected department loaded
    return render_template("edit_department.html", data=data)


@app.route("/departments/<oid>", methods=["PUT"])
def update_department(oid):
    """The update the department"""

    new_department_name = request.form.get("department_name")

    # Update the department
    Departments.update({Departments.name: new_department_name}).where(
        Departments.id == oid
    ).execute()

    # Get the new value and send it to the user
    data = Departments.select().where(Departments.id == oid).get()

    # Send the department table row with the selected department loaded
    return render_template("view_department.html", data=data)


@app.route("/departments/<oid>", methods=["DELETE"])
def delete_department(oid):
    """Delete the department"""

    # Delete the department in the database
    try:
        Departments.delete().where(Departments.id == oid).execute()
    except IntegrityError as e:
        return (f"Failed to delete the department: <br>{e}", 500)

    # return them to the updated department list
    return redirect(url_for("departments_index"), 303)


@app.route("/performance_plans")
def performance_plans_browse():
    """Browse page for performance plans"""

    # Local vars
    data = {}
    data["pips"] = []
    pips = Pips.select()

    for pip in pips:
        pip = model_to_dict(pip)
        pip["task_count"] = PipTasks.select().where(PipTasks.pip == pip["id"]).count()
        data["pips"].append(pip)

    # Performance Plan Template
    return render_template("performance_plans.html", data=data)


@app.route("/add_pip")
def add_pip():
    """Display the add pip form"""

    # Local vars
    data = {}
    data["statuses"] = PipStatuses.select()

    return render_template("pip_add.html", data=data)


@app.route("/pips", methods=["POST"])
def create_pip():
    """Make a new PIP in the database"""

    # Get the user submitted values
    employee = request.form.get("employee")
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")
    status = request.form.get("pip_status")
    manager = request.form.get("manager")
    hr_rep = request.form.get("hr")

    current_app.logger.debug(status)

    # Verify that they submitted actual values
    if not employee or not manager or not hr_rep:
        flash("No person selected")
        return redirect(url_for("add_pip"))
    elif not status:
        flash("No status selected")
        return redirect(url_for("add_pip"))

    # We need the database ids for these fields
    try:
        db_employee = Employees.select().where(Employees.name == employee).get()
        db_manager = Employees.select().where(Employees.name == manager).get()
        db_hr_rep = Employees.select().where(Employees.name == hr_rep).get()
    except DoesNotExist:
        flash("Invalid person selected")
        return redirect(url_for("add_pip"))

    # Create the new record
    Pips.create(
        employee=db_employee.id,
        manager=db_manager.id,
        hr_rep=db_hr_rep.id,
        status=status,
        start_date=start_date,
        end_date=end_date,
    )

    return redirect(url_for("performance_plans_browse"))


@app.route("/pip/<pid>", methods=["GET"])
def read_pip(pid):
    """Details page for a PIP"""

    # Local Vars
    data = {}

    # the information for this specific pip
    data["pip"] = Pips.select().where(Pips.id == pid).get()

    # Get the tasks for this pip
    data["tasks"] = PipTasks.select().where(PipTasks.pip == pid)

    # loaded in a template and sent via HTMX
    return render_template("pip_read.html", data=data)


@app.route("/pip/new_task/<pid>")
def new_pip_task_form(pid):
    """Send the new task form via HTMX"""

    # Local Vars
    data = {}

    # the information for this specific pip
    data["pip"] = Pips.select().where(Pips.id == pid).get()

    # The PIP Task Statuses
    data["task_grades"] = PipTaskGrades.select()

    # New task form sent via HTMX
    return render_template("pip_new_task.html", data=data)


@app.route("/pip/task", methods=["POST"])
def save_new_pip_task():
    """Save the new PIP Task"""

    # Get the values from the user
    pid = request.form.get("pid")
    task = request.form.get("task")
    due_date = request.form.get("due_date")
    progress = request.form.get("progress")
    grade = request.form.get("grade")

    # Create the record with or without the grade
    if not grade:
        PipTasks.create(pip=pid, task=task, due_date=due_date, progress=progress)
    else:
        PipTasks.create(
            pip=pid, task=task, due_date=due_date, progress=progress, grade=grade
        )

    return redirect(url_for("read_pip", pid=pid))


@app.route("/pip/task/edit/<tid>")
def edit_pip_task(tid):
    """Edit form for a PIP Task"""

    # Local Vars
    data = {}

    # Get the data for this task
    data["task"] = PipTasks.select().where(PipTasks.id == tid).get()

    # The PIP Task Statuses
    data["task_grades"] = PipTaskGrades.select()

    # Send back the edit form with the task loaded
    return render_template("pip_edit_task.html", data=data)


@app.route("/pip/task/<tid>", methods=["PUT"])
def update_pip_task(tid):
    """Update an editted PIP Task"""

    # Local Vars
    update_record = {}

    # Get the values from the user
    pid = request.form.get("pid")
    task = request.form.get("task")
    due_date = request.form.get("due_date")
    progress = request.form.get("progress")
    grade = request.form.get("grade")

    # Update the record in the database
    if len(grade) > 2:  # Don't send grade if they have't assigned one
        update_record = {
            PipTasks.task: task,
            PipTasks.due_date: due_date,
            PipTasks.progress: progress,
        }
    else:
        update_record = {
            PipTasks.task: task,
            PipTasks.due_date: due_date,
            PipTasks.progress: progress,
            PipTasks.grade: grade,
        }
    PipTasks.update(update_record).where(PipTasks.id == tid).execute()

    # Send them back to the PIP details
    current_app.logger.debug(url_for("read_pip", pid=pid))
    return redirect(url_for("read_pip", pid=pid), 303)


@app.route("/pip/task/<tid>", methods=["DELETE"])
def delete_pip_task(tid):
    """Delete a PIP Task"""

    # We need to figure out with pip goes with this task id
    pip_task = PipTasks.select().where(PipTasks.id == tid).get()

    # Now we need to delete the PIP Task in the database
    PipTasks.delete().where(PipTasks.id == tid).execute()

    # And redirect back to the PIP details page where we were
    return redirect(url_for("read_pip", pid=pip_task.pip.id), 303)


@app.route("/edit_pip/<pid>")
def edit_pip(pid):
    """edit form for a PIP"""

    # The information for this specific PIP
    data = {}
    data["pip"] = Pips.select().where(Pips.id == pid).get()
    data["statuses"] = PipStatuses.select()

    # loaded in a template and sent via HTMX
    return render_template("pip_edit.html", data=data)


@app.route("/pip/<pid>", methods=["PUT"])
def save_pip(pid):
    """Save updates to a PIP"""

    # Get the user submitted values
    employee = request.form.get("employee")
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")
    status = request.form.get("pip_status")
    manager = request.form.get("manager")
    hr_rep = request.form.get("hr")

    # Verify that they submitted actual values
    if not employee or not manager or not hr_rep:
        flash("No person selected")
        return redirect(url_for("add_pip"), 303)
    elif not status:
        flash("No status selected")
        return redirect(url_for("add_pip"), 303)

    # We need the database ids for these fields
    try:
        db_employee = Employees.select().where(Employees.name == employee).get()
        db_manager = Employees.select().where(Employees.name == manager).get()
        db_hr_rep = Employees.select().where(Employees.name == hr_rep).get()
    except DoesNotExist:
        flash("Invalid person selected")
        return redirect(url_for("add_pip"), 303)

    # Update them in the database
    Pips.update(
        {
            Pips.employee: db_employee,
            Pips.start_date: start_date,
            Pips.end_date: end_date,
            Pips.status: status,
            Pips.manager: db_manager,
            Pips.hr_rep: db_hr_rep,
        }
    ).where(Pips.id == pid).execute()

    # Let's get the updated information for this PIP
    data = {}
    data["pip"] = Pips.select().where(Pips.id == pid).get()

    # loaded in a template and sent via HTMX
    return render_template("pip_read.html", data=data)


@app.route("/pip/<pid>", methods=["DELETE"])
def delete_pip(pid):
    """Delete a PIP"""

    # Delete any PIP associated tasks

    # Delete the PIP
    Pips.delete().where(Pips.id == pid).execute()

    return redirect(url_for("performance_plans_browse"), 303)


# Helper functions =============================================================
@app.route("/employee_search/<keyword>", methods=["POST"])
def employee_search(keyword):
    """HTMX powered: Return a list of employee names"""

    # Local vars
    data = {}

    # What have they searched for so far?
    s = request.form.get(keyword)

    # If they haven't sent characters don't send anything
    if len(s) > 0:
        data["employees"] = Employees.select().where(Employees.name.startswith(s))

    return render_template("employee_results.html", data=data, keyword=keyword)


@app.route("/onboarding/checklist")
def onboarding_checklist():
    """Onboarding checklist templates"""

    # local vars
    data = {}

    # Get the departments
    data["departments"] = Departments.select()

    # loaded in a template and sent via HTMX
    return render_template("onboarding_checklist.html", data=data)


@app.route("/onboarding/checklist/department")
def onboarding_checklist_department():
    """Onboarding checklist templates"""

    # local vars
    data = {}

    # Let's retrieve the checklist for the request department
    dept_id = request.form.get("department")
    checklist = OnboardingChecklists.select().where(OnboardingChecklists.department == dept_id)

    # loaded in a template and sent via HTMX
    return render_template("onboarding_department_checklist.html", data=data)


@app.route("/onboarding/checklist/new/form")
def onboarding_checklist_new_form():
    """Onboarding checklist new task form"""

    # local vars
    data = {}

    # Get the departments
    data["departments"] = Departments.select()

    # loaded in a template and sent via HTMX
    return render_template("onboarding_checklist_new_form.html", data=data)
