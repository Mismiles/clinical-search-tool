import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "PharmacyLinks"
app.config["MONGO_URI"] = os.getenv("MONGODB_LIST")

mongo = PyMongo(app)

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
    return render_template("resourcelist.html", resource=mongo.db.resource.find())

@app.route("/addresource")
def addresource():
    return render_template("addresource.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)