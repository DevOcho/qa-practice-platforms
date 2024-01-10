#!/usr/bin/env python3

import os

# Bread Project Libraries
from model import db, Departments, EmployeeStatuses, Employees, Offices

# Removing the current database
if os.path.isfile("employees.db"):
    os.remove("employees.db")

# Talk to the user
print("Initializing the Database")

# =============================================================================
# Connect to the database
db.connect()

# Create the tables
print("  - Creating tables...".ljust(40), end="")
db.create_tables([Departments, Offices, EmployeeStatuses, Employees])
print(" done")


# => Offices ------------------------------------------------------------------
print("  - Creating Offices...".ljust(40), end="")
offices = [
    {"name": "Santiago"},
    {"name": "Moca"},
    {"name": "La Vega"},
    {"name": "San Francisco de Macoris"},
    {"name": "Tamboril"},
    {"name": "Salcedo"},
    {"name": "Tenares"},
    {"name": "Villa Bisonó"},
    {"name": "Esperanza"},
    {"name": "Mao"},
    {"name": "Luperon"},
]
with db.atomic():
    Offices.insert_many(offices).execute()  # pylint: disable=no-value-for-parameter
print(" done")


# => Departments --------------------------------------------------------------
print("  - Creating Departments...".ljust(40), end="")
departments = [
    {"name": "Recursos Humanos"},
]
with db.atomic():
    Departments.insert_many(  # pylint: disable=no-value-for-parameter
        departments
    ).execute()
print(" done")


# => Employee Statuses --------------------------------------------------------
print("  - Creating Employee Statuses...".ljust(40), end="")
employee_statuses = [
    {"name": "Hired - Not Onboarded"},
    {"name": "Employed"},
    {"name": "Fired"},
    {"name": "Quit"},
]
with db.atomic():
    EmployeeStatuses.insert_many(  # pylint: disable=no-value-for-parameter
        employee_statuses
    ).execute()
print(" done")

# Close the database connection
db.close()
