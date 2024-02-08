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
    {"name": "Leroy Jenkins", "department": 6, "office": 3, "hire_date": "2022-07-01", "status": 2},
    {"name": "Gustavo Garcia", "department": 6, "office": 3, "hire_date": "2020-03-04", "status": 2},
    {"name": "Lisa Allgood", "department": 2, "office": 1, "hire_date": "2023-05-15", "status": 2},
    {"name": "Sara Gonzales", "department": 1, "office": 1, "hire_date": "2008-09-30", "status": 2},
    {"name": "Maria Sanchez", "department": 1, "office": 1, "hire_date": "2022-05-24", "status": 2},
    {"name": "Kenny Pyatt", "department": 7, "office": 1, "hire_date": "2022-12-04", "status": 1},
]
with db.atomic():
    Employees.insert_many(employees).execute()  # pylint: disable=no-value-for-parameter
print(" done")


# => Onboading Checklists ------------------------------------------------------
print("  - Creating Onboarding Checklists...".ljust(50), end="")
checklists = [
    # Executive Tasks (these are first to make a bug more obvious)
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

]
with db.atomic():
    OnboardingChecklists.insert_many(
        checklists
    ).execute()  # pylint: disable=no-value-for-parameter
print(" done")



# => Employee Onboarding Checklist ----------------------------------------------
print("  - Creating Employee Onboarding Checklists...".ljust(50), end="")
checklists = [
    # Kenny's Onboarding (this is first to make a bug more obvious)
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
    # Leroy's Onboarding
    {
        "task": "Welcome Email",
        "timeframe": "prestart",
        "employee": 1,
        "assigned_employee": 4,
        "department": 1,
        "status": "done"
    },
    {
        "task": "Office Tour",
        "timeframe": "first30",
        "employee": 1,
        "assigned_employee": 4,
        "department": 1,
        "status": "done"
    },
    {
        "task": "Information Security Training",
        "timeframe": "second30",
        "employee": 1,
        "assigned_employee": 6,
        "department": 3,
        "status": "done"
    },
    {
        "task": "Customer Site Visit",
        "timeframe": "third30",
        "employee": 1,
        "assigned_employee": 6,
        "department": 6,
        "status": "done"
    },
    # Gustavo's Onboarding
    {
        "task": "Welcome Email",
        "timeframe": "prestart",
        "employee": 2,
        "assigned_employee": 4,
        "department": 1,
        "status": "done"
    },
    {
        "task": "Office Tour",
        "timeframe": "first30",
        "employee": 2,
        "assigned_employee": 4,
        "department": 1,
        "status": "done"
    },
    {
        "task": "Information Security Training",
        "timeframe": "second30",
        "employee": 2,
        "assigned_employee": 6,
        "department": 3,
        "status": "done"
    },
    {
        "task": "Customer Site Visit",
        "timeframe": "third30",
        "employee": 2,
        "assigned_employee": 6,
        "department": 6,
        "status": "done"
    },
    # Lisa's Onboarding
    {
        "task": "Welcome Email",
        "timeframe": "prestart",
        "employee": 3,
        "assigned_employee": 4,
        "department": 1,
        "status": "done"
    },
    {
        "task": "Office Tour",
        "timeframe": "first30",
        "employee": 3,
        "assigned_employee": 4,
        "department": 1,
        "status": "done"
    },
    {
        "task": "Information Security Training",
        "timeframe": "second30",
        "employee": 3,
        "assigned_employee": 6,
        "department": 3,
        "status": "done"
    },
    {
        "task": "Read The Law can be fun by Henry Boardom",
        "timeframe": "third30",
        "employee": 3,
        "assigned_employee": 6,
        "department": 2,
        "status": "done"
    },
    # Sara's Onboarding
    {
        "task": "Welcome Email",
        "timeframe": "prestart",
        "employee": 4,
        "assigned_employee": 4,
        "department": 1,
        "status": "done"
    },
    {
        "task": "Office Tour",
        "timeframe": "first30",
        "employee": 4,
        "assigned_employee": 4,
        "department": 1,
        "status": "done"
    },
    {
        "task": "Information Security Training",
        "timeframe": "second30",
        "employee": 4,
        "assigned_employee": 6,
        "department": 3,
        "status": "done"
    },
    # Maria's Onboarding
    {
        "task": "Welcome Email",
        "timeframe": "prestart",
        "employee": 5,
        "assigned_employee": 4,
        "department": 1,
        "status": "done"
    },
    {
        "task": "Office Tour",
        "timeframe": "first30",
        "employee": 5,
        "assigned_employee": 4,
        "department": 1,
        "status": "done"
    },
    {
        "task": "Information Security Training",
        "timeframe": "second30",
        "employee": 5,
        "assigned_employee": 6,
        "department": 3,
        "status": "done"
    },
    {
        "task": "Count the beans",
        "timeframe": "third30",
        "employee": 5,
        "assigned_employee": 6,
        "department": 5,
        "status": "done"
    },
]
with db.atomic():
    EmployeeOnboardingChecklists.insert_many(
        checklists
    ).execute()  # pylint: disable=no-value-for-parameter
print(" done")


# Close the database connection
db.close()
