"""
  This is the model for our database.  This is for peewee objects only.
"""

from datetime import datetime

from peewee import (
    AutoField,
    BooleanField,
    CharField,
    DateTimeField,
    Model,
    SqliteDatabase,
)

db = SqliteDatabase("employee.db")


# We will only have one database so let's make a base class and use it everywhere
class BaseModel(Model):
    """This is the base model so every model inherits the db connection"""

    class Meta:
        """Peewee Configuration"""

        database = db
        legacy_table_names = False


class employee(BaseModel):
    """employee is the table that will hold our employee records"""

    id = AutoField(primary_key=True)
    name = CharField()
    title = CharField()
    fired = BooleanField(default=False)
    hired_at = DateTimeField(null=True)
    fired_at = DateTimeField(null=True)
