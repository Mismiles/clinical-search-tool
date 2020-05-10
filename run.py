import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from os import path
if path.exists("env.py"):
    import env

app.config[MONGODB_LIST] = os.getenv("MONGODB_LIST")
app.config[DBS_NAME] = "PharmacyLinks"

mongo = PyMongo(app)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results")
def results():
    return render_template("result.html", search_terms=mongo.db.tasks.find())

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/resourcelist")
def resourcelist():
    return render_template("resourcelist.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)