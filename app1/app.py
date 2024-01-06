from flask import Flask, render_template
from model import db

app = Flask(__name__, static_folder="static", static_url_path="")

@app.route('/')
def index():

    # Local vars
    data = {}

    return render_template("index.html", data=data)
