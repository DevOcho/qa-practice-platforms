from flask import Flask, render_template

from rest_api import employee
from rest_api.model import db

app = Flask(__name__, static_folder="static", static_url_path="/static")


# Database ====================================================================
@app.before_request
def setup_application():
    """Do the things we need to have an application"""
    db.connect()


@app.teardown_request
def close_db_connection(exc):
    """When the request stops let's politely stop the db connection (return it to the pool)"""

    if not db.is_closed():
        db.close()


# Documentation ===============================================================
@app.route("/")
def documentation():
    """Return the swagger docs for this api"""

    return render_template("docs.html")

# Blueprints ==================================================================
app.register_blueprint(employee.employee_bp)
