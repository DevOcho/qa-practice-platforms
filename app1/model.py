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
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ThreadSafeDatabaseMetadata


# Setup the database connection
db = PooledMySQLDatabase(
        "app1",
        user="root",
        password="qa_tester",
        host="qa-test-db",
        port=3306,
        max_connections=32,
        stale_timeout=180,
)


# We will only have one database so let's make a base class and use it everywhere
class BaseModel(Model):
    """This is the base model so every model inherits the db connection"""

    class Meta:
        """Peewee Configuration"""

        database = db
        legacy_table_names = False
        model_metadata_class = ThreadSafeDatabaseMetadata


class Employees(BaseModel):
    """ The Employees table """

    name = CharField()
    department = CharField()
    office = CharField()
    years = IntegerField()
    status = ForeignKeyField(EmployeeStatuses, backref="employee_statuses")


class EmployeeStatuses(BaseModel):
    """ The statuses an employee can have"""

    name = CharField()
