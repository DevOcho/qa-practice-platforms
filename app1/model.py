from peewee import (
    AutoField,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    Field,
    FloatField,
    ForeignKeyField,
    IntegerField,
    Model,
    TextField,
)
from playhouse.pool import SqliteDatabase
from playhouse.shortcuts import ThreadSafeDatabaseMetadata


# Setup the database connection
db = SqliteDatabase("employees.db")


# We will only have one database so let's make a base class and use it everywhere
class BaseModel(Model):
    """This is the base model so every model inherits the db connection"""

    class Meta:
        """Peewee Configuration"""

        database = db
        legacy_table_names = False
        model_metadata_class = ThreadSafeDatabaseMetadata


class Departments(BaseModel):
    """The departments in the company"""

    name = CharField()


class Offices(BaseModel):
    """The offices in the company"""

    name = CharField()


class EmployeeStatuses(BaseModel):
    """The statuses an employee can have"""

    name = CharField()


class Employees(BaseModel):
    """The Employees table"""

    name = CharField()
    department = ForeignKeyField(Departments, backref="departments")
    office = ForeignKeyField(Offices, backref="offices")
    years = IntegerField()
    status = ForeignKeyField(EmployeeStatuses, backref="employee_statuses")
