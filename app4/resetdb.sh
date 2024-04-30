#!/bin/bash

# Inform the user we are starting
echo -e "Resetting the database\n"

# Remove the current database
rm -f employee.db

# Initialize the database (create tables)
./initdb.py

# Add a newline between the commands to make the output cleaner
echo ""

# Seed the database (load test data)
./seed.py

# Inform the user we are finished
echo -e "\nDatabase Reset"
