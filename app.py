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
    return render_template("addresource.html",categories=mongo.db.categories.find())

@app.route("/insertresource", methods=['POST'])
def insertresource():
    resource = mongo.db.resource
    resource.insert_one(request.form.to_dict())
    return redirect(url_for("resourcelist"))

@app.route("/editresource/<resource_id>")
def editresource(resource_id):
    the_resource = mongo.db.resource.find_one({"_id": ObjectId(resource_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editresource.html', resource=the_resource, categories=all_categories)

@app.route("/updateresource/<resource_id>", methods=["POST"])
def updateresource(resource_id):
    resources = mongo.db.resource
    resources.update( {'_id': ObjectId(resource_id)},
    {
        'resource_category':request.form.get('resource_category'),
        'resource_name':request.form.get('resource_name'),
        'resource_link':request.form.get('resource_link'),
        'resource_description': request.form.get('resource_description'),
        'resource_updated': request.form.get('resource_updated')
    })
    return redirect(url_for('resourcelist'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)