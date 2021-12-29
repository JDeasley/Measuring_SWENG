from github import Github
import os

from faker import Faker
from collections import defaultdict
faker = Faker()
fake = defaultdict(faker.name)

token = os.getenv('GITHUB_PAT')
g = Github(token)
# usr = None

def get_user():
    try:
        usr = g.get_user()
    except Exception:
        usr = None

    return usr

def get_named_user(name):
    try:
        usr = g.get_user(name)
    except Exception:
        usr = None

    return usr

def create_user_dict(user):
    try:
        dct = {
            'user':         fake[user.login].replace(" ",""),
            'fullname':     fake[user.name],
            'location':     user.location,
            'company':      user.company,
            'public_repos': user.public_repos
        }

        for k, v in dict(dct).items():
            if v is None:
                del dct[k]
    
    except Exception:
        dct = None

    return dct

def get_named_repo(repo_name):
    try:
        repo = g.get_repo(repo_name)
    except Exception:
        repo = None

    return repo
