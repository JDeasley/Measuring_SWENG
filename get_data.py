from github import Github
import os

token = os.getenv('GITHUB_PAT')
g = Github(token)
usr = None

def get_real_user(self):
    usr = g.get_user()
    return g



