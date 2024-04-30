"""Todo Blueprint"""

import re

from flask import Blueprint, request
from peewee import DoesNotExist
from playhouse.shortcuts import model_to_dict

from rest_api.model import employee

employee_bp = Blueprint(
    "employee", __name__, template_folder="templates", url_prefix="/employee"
)


@employee_bp.route("/")
def get_employees():
    """The GET mode for all employees"""

    # Get all the employees as a list of dictionaries
    employee_list = list(employee.select().dicts())

    # Return the template with tasks loaded
    return employee_list


@employee_bp.route("/<eid>")
def get_single_employee(eid):
    """The GET mode for a single employee"""

    # Get a single employee and convert it to a dictionary
    try:
        single_employee = model_to_dict(
            employee.select().where(employee.id == eid).get()
        )

    # If we didn't find the record, let them know
    except DoesNotExist:
        return "", 404

    # Return JSON for a single employee
    return single_employee


@employee_bp.route("/", methods=["POST"])
def create_employee():
    """Create a single employee"""

    # Local Vars
    name = request.form.get("name")
    title = request.form.get("title")
    fired = request.form.get("fired")
    hired_at = request.form.get("hired_at")
    fired_at = request.form.get("fired_at")

    # We need to convert fired to a Boolean
    fired = bool(re.search(fired, "true", re.IGNORECASE))

    # Save the record to the database
    new_employee = employee.create(
        name=name, title=title, fired=fired, hired_at=hired_at, fired_at=fired_at
    )
    new_employee.save()

    return model_to_dict(new_employee), 201


@employee_bp.route("/<eid>", methods=["PUT"])
def update_full_employee(eid):
    """Update an entire single employee record"""

    name = request.form.get("name")
    title = request.form.get("title")
    fired = request.form.get("fired")
    hired_at = request.form.get("hired_at")
    fired_at = request.form.get("fired_at")

    # We need to convert fired to a Boolean
    fired = bool(re.search(fired, "true", re.IGNORECASE))

    # Save the record to the database
    save_employee = employee.update(
        name=name, title=title, fired=fired, hired_at=hired_at, fired_at=fired_at
    ).where(employee.id == eid)
    save_employee.execute()

    # The best practice is to return the item that was changed so we need to get it
    updated_employee = employee.select().where(employee.id == eid).get()

    return model_to_dict(updated_employee)


@employee_bp.route("/<eid>", methods=["DELETE"])
def delete_employee(eid):
    """Delete a single employee"""

    # Delete a single record
    employee.delete().where(employee.id == eid).execute()

    return "", 204


@employee_bp.route("/<eid>", methods=["PATCH"])
def update_employee(eid):
    """Update part of a single employee record"""

    # Local Vars
    update_items = {}

    # set the value if they sent in the list, otherwise ignore it
    if "name" in request.form:
        update_items["name"] = request.form.get("name")

    if "title" in request.form:
        update_items["title"] = request.form.get("title")

    if "fired" in request.form:
        # We need fired to be a Boolean
        update_items["fired"] = bool(
            re.search(request.form.get("fired"), "true", re.IGNORECASE)
        )

    if "hired_at" in request.form:
        update_items["hired_at"] = request.form.get("hired_at")

    if "fired_at" in request.form:
        update_items["fired_at"] = request.form.get("fired_at")

    # Save the record to the database
    save_employee = employee.update(update_items).where(employee.id == eid)
    save_employee.execute()

    # The best practice is to return the item that was changed so we need to get it
    updated_employee = employee.select().where(employee.id == eid).get()

    # Send back a JSON response with the success code
    return model_to_dict(updated_employee)
