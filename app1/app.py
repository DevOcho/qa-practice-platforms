from flask import Flask, render_template, redirect, url_for, request, current_app
from model import db, EmployeeStatuses, Employees, Departments, Offices

app = Flask(__name__, static_folder="static", static_url_path="")


@app.route("/")
def index():
    """Site Index"""

    # Local vars
    data = {}

    # Get the list of employees
    data["employees"] = Employees.select()

    for employee in data["employees"]:
        current_app.logger.debug(employee)

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
