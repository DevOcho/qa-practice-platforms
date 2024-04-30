#!/usr/bin/env python3

# Bread Project Libraries
from rest_api.model import employee, db

# Talk to the user
print("Initializing the Database")

# =============================================================================
# Connect to the database
db.connect()

# Create the tables
print("  - Creating tables...", end="")
db.create_tables([employee])
print(" done")

# Close the database connection
db.close()
