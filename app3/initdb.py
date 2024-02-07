#!/usr/bin/env python3

import os

# Bread Project Libraries
from model import (
    db,
    Departments,
    EmployeeOnboardingChecklists,
    EmployeeStatuses,
    Employees,
    Offices,
    OnboardingChecklists,
    PipStatuses,
    Pips,
    PipTaskGrades,
    PipTasks
)

# Removing the current database
if os.path.isfile("employees.db"):
    os.remove("employees.db")

# Talk to the user
print("Initializing the Database")

# =============================================================================
# Connect to the database
db.connect()

# Create the tables
print("  - Building Tables...".ljust(50), end="")
db.create_tables(
    [
        Departments,
        Offices,
        EmployeeStatuses,
        Employees,
        PipStatuses,
        Pips,
        PipTaskGrades,
        PipTasks,
        OnboardingChecklists,
        EmployeeOnboardingChecklists
    ]
)
print(" done")


# => Offices ------------------------------------------------------------------
print("  - Creating Offices...".ljust(50), end="")
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
print("  - Creating Departments...".ljust(50), end="")
departments = [
    {"name": "Human Resources"},
    {"name": "Legal"},
    {"name": "Technology"},
    {"name": "Operations"},
    {"name": "Finanace"},
    {"name": "Sales"},
    {"name": "Executive"},
]
with db.atomic():
    Departments.insert_many(  # pylint: disable=no-value-for-parameter
        departments
    ).execute()
print(" done")


# => Employee Statuses --------------------------------------------------------
print("  - Creating Employee Statuses...".ljust(50), end="")
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


# => PIP Statuses -------------------------------------------------------------
print("  - Creating PIP Statuses...".ljust(50), end="")
pip_statuses = [
    {"name": "Proposed"},
    {"name": "In Progress"},
    {"name": "Completed - Success"},
    {"name": "Completed - Failure"},
]
with db.atomic():
    PipStatuses.insert_many(  # pylint: disable=no-value-for-parameter
        pip_statuses
    ).execute()
print(" done")

# => PIP Task Grades ----------------------------------------------------------
print("  - Creating PIP Task Grades...".ljust(50), end="")
pip_task_grades = [
    {"name": "A+"},
    {"name": "A"},
    {"name": "A-"},
    {"name": "B+"},
    {"name": "B"},
    {"name": "B-"},
    {"name": "C"},
    {"name": "D"},
    {"name": "F"},
]
with db.atomic():
    PipTaskGrades.insert_many(  # pylint: disable=no-value-for-parameter
        pip_task_grades
    ).execute()
print(" done")

# Close the database connection
db.close()
