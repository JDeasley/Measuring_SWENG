from flask import Flask, render_template
import os
import json

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

def fetch_data():
    f = open('data.json')
    rdata = json.load(f)

    return rdata

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/repo/<path:repo_name>")
def show_repo(repo_name):
    data = fetch_data()
    first_user = data[0]["user"]
    return render_template("test.html", **locals())
