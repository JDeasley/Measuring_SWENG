from flask import Flask, render_template
import os
import json
import get_data, cleardb, read_data

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
repos_fetched = []
cleardb.main()

def fetch_data(repo_name):
    if repo_name in repos_fetched:
        print("Already fetched repo: ", repo_name)
    else:
        # 1. Try to fetch data from DB for this repo
        print("Fetching repo: ", repo_name)
        get_data.fetch(repo_name)
        repos_fetched.append(repo_name)

        # f = open('data.json')
        # rdata = json.load(f)

    rdata = read_data.db_fetch(repo_name)
    return rdata

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/repo/<path:repo_name>")
def show_repo(repo_name):
    data = fetch_data(repo_name)
    first_user = data[0]["user"]
    return render_template("repo.html", **locals())
