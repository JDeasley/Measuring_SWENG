from github import Github
import os

token = os.getenv('GITHUB_PAT')
g = Github(token)
usr = None

def get_user():
    usr = g.get_user()
    return g
