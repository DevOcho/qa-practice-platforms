#!/usr/bin/env python3

# Python standard imports
from datetime import datetime

# Import the tables and database connection
from rest_api.model import employee, db

# Let the user know what is going on
print("Seeding the database")

# Connect to the database
db.connect()

# Load employees into the employee table
print("  - Creating Employees...", end="")
employee.create(name="Bill Jenkins", title="CEO", hired_at=datetime.now())
employee.create(name="Mark Cleaner", title="Janitor", hired_at=datetime.now())
employee.create(name="Sara Gonzales", title="Accountant", hired_at=datetime.now())
print(" done")

# Close the database connection
db.close()
