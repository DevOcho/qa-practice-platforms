#!/usr/bin/env python3

import os

# Bread Project Libraries
from model import (
    db,
    Departments,
    EmployeeStatuses,
    Employees,
    Offices,
    OnboardingChecklists,
    OnboardingEmployeeChecklists,
    PipStatuses,
    Pips,
    PipTaskGrades,
    PipTasks
)

# ==============================================================================
# Connect to the database
db.connect()

# => Employees -----------------------------------------------------------------
print("  - Creating Employees...".ljust(40), end="")
employees = [
    {"name": "Leroy Jenkins", "department": 6, "office": 3, "years": 3, "status": 2},
    {"name": "Gustavo Garcia", "department": 6, "office": 3, "years": 7, "status": 2},
    {"name": "Lisa Allgood", "department": 2, "office": 1, "years": 2, "status": 2},
    {"name": "Sara Gonzales", "department": 1, "office": 1, "years": 12, "status": 2},
    {"name": "Maria Sanchez", "department": 1, "office": 1, "years": 4, "status": 2},
]
with db.atomic():
    Employees.insert_many(employees).execute()  # pylint: disable=no-value-for-parameter
print(" done")

# Close the database connection
db.close()
