import flask
import json
import os

app = flask.Flask(__name__)
navitems = {}
projects = {}

@app.before_first_request
def init():
    global navitems, projects
    with open("manifest.json", "r") as jsonfile:
        manifest = json.loads(jsonfile.read())
    navitems = manifest["navitems"]
    projects = manifest["projects"]

@app.context_processor
def context_processor():
    return {"os": os, "navitems": navitems, "projects": projects}

@app.errorhandler(404)
def notfound(error):
    return flask.render_template("notfound.html")

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/contact/")
def contact():
    return flask.render_template("contact.html")

@app.route("/project/")
def projectlist():
    return flask.render_template("project/index.html")

@app.route("/project/<string:project>/")
def project(project):
    template = f"project/{project}/index.html"
    if not project in projects or not os.path.exists(f"./templates/{template}"):
        return flask.abort(404)
    return flask.render_template(template, project=projects[project])