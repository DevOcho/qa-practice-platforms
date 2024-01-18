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


# Setup the database connection
db = SqliteDatabase("employees.db", pragmas={"foreign_keys": 1})


# We will only have one database so let's make a base class and use it everywhere
class BaseModel(Model):
    """This is the base model so every model inherits the db connection"""

    class Meta:
        """Peewee Configuration"""

        database = db
        legacy_table_names = False


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


class PipStatuses(BaseModel):
    """ Statuses for Pips"""

    name = CharField()


class Pips(BaseModel):
    """ Performance Improvement Plans"""

    employee = ForeignKeyField(Employees, backref="employees")
    manager = ForeignKeyField(Employees, backref="employees")
    hr_rep = ForeignKeyField(Employees, backref="employees")
    status = ForeignKeyField(PipStatuses, backref="statuses")
    start_date = DateField()
    end_date = DateField()


class PipTaskGrades(BaseModel):
    """Grades for the completed Pip Tasks"""

    name = CharField()


class PipTasks(BaseModel):
    """ Tasks assigned to a Pip"""

    task = CharField()
    due_date = DateField()
    progress = IntegerField()
    grade = ForeignKeyField(PipTaskGrades, backref="pip_task_grades")
