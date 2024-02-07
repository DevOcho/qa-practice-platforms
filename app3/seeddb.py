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
    PipTasks,
)

# ==============================================================================
# Connect to the database
db.connect()

# => Employees -----------------------------------------------------------------
print("  - Creating Employees...".ljust(50), end="")
employees = [
    {"name": "Leroy Jenkins", "department": 6, "office": 3, "years": 3, "status": 2},
    {"name": "Gustavo Garcia", "department": 6, "office": 3, "years": 7, "status": 2},
    {"name": "Lisa Allgood", "department": 2, "office": 1, "years": 2, "status": 2},
    {"name": "Sara Gonzales", "department": 1, "office": 1, "years": 12, "status": 2},
    {"name": "Maria Sanchez", "department": 1, "office": 1, "years": 4, "status": 2},
    {"name": "Kenny Pyatt", "department": 7, "office": 1, "years": 3, "status": 1},
]
with db.atomic():
    Employees.insert_many(employees).execute()  # pylint: disable=no-value-for-parameter
print(" done")


# => Onboading Checklists ------------------------------------------------------
print("  - Creating Onboarding Checklists...".ljust(50), end="")
checklists = [
    # HR Tasks
    {
        "task": "Welcome Email",
        "timeframe": "prestart",
        "department": 1,
        "assigned_department": 1,
    },
    {
        "task": "Office Tour",
        "timeframe": "first30",
        "department": 1,
        "assigned_department": 1,
    },

    # Legal
    {
        "task": "Welcome Email",
        "timeframe": "prestart",
        "department": 2,
        "assigned_department": 1,
    },
    {
        "task": "Office Tour",
        "timeframe": "first30",
        "department": 2,
        "assigned_department": 1,
    },

    # Technology
    {
        "task": "Welcome Email",
        "timeframe": "prestart",
        "department": 3,
        "assigned_department": 1,
    },
    {
        "task": "Office Tour",
        "timeframe": "first30",
        "department": 3,
        "assigned_department": 1,
    },

    # Operations
    {
        "task": "Welcome Email",
        "timeframe": "prestart",
        "department": 4,
        "assigned_department": 1,
    },
    {
        "task": "Office Tour",
        "timeframe": "first30",
        "department": 4,
        "assigned_department": 1,
    },

    # Finance
    {
        "task": "Welcome Email",
        "timeframe": "prestart",
        "department": 5,
        "assigned_department": 1,
    },
    {
        "task": "Office Tour",
        "timeframe": "first30",
        "department": 5,
        "assigned_department": 1,
    },

    # Sales
    {
        "task": "Welcome Email",
        "timeframe": "prestart",
        "department": 6,
        "assigned_department": 1,
    },
    {
        "task": "Office Tour",
        "timeframe": "first30",
        "department": 6,
        "assigned_department": 1,
    },
    {
        "task": "Book lunch meeting with VP of Sales",
        "timeframe": "second30",
        "department": 6,
        "assigned_department": 1,
    },

    # Executive Tasks
    {
        "task": "Welcome Gift Basket",
        "timeframe": "prestart",
        "department": 7,
        "assigned_department": 1,
    },
    {
        "task": "Office Tour",
        "timeframe": "first30",
        "department": 7,
        "assigned_department": 1,
    },
    {
        "task": "USA Office Visit",
        "timeframe": "second30",
        "department": 7,
        "assigned_department": 7,
    },
    {
        "task": "Customer Site Visit",
        "timeframe": "third30",
        "department": 7,
        "assigned_department": 7,
    },
]
with db.atomic():
    OnboardingChecklists.insert_many(
        checklists
    ).execute()  # pylint: disable=no-value-for-parameter
print(" done")



# => Employee Onboarding Checklist ----------------------------------------------
print("  - Creating Employee Onboarding Checklists...".ljust(50), end="")
checklists = [
    # Kenny's Onboarding
    {
        "task": "Welcome Gift Basket",
        "timeframe": "prestart",
        "employee": 6,
        "assigned_employee": 4,
        "department": 1,
        "status": "to-do"
    },
    {
        "task": "Office Tour",
        "timeframe": "first30",
        "employee": 6,
        "assigned_employee": 4,
        "department": 1,
        "status": "to-do"
    },
    {
        "task": "USA Office Visit",
        "timeframe": "second30",
        "employee": 6,
        "assigned_employee": 6,
        "department": 7,
        "status": "to-do"
    },
    {
        "task": "3x Customer Site Visits",
        "timeframe": "third30",
        "employee": 6,
        "assigned_employee": 6,
        "department": 7,
        "status": "to-do"
    },
]
with db.atomic():
    EmployeeOnboardingChecklists.insert_many(
        checklists
    ).execute()  # pylint: disable=no-value-for-parameter
print(" done")


# Close the database connection
db.close()
