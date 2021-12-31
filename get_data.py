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

def create_repo_dict(repo):
    try:
        dct = {
            'name':         repo.name,
            'owner':        fake[repo.owner.login].replace(" ",""),
            'description':  repo.description,
            'stars':        repo.stargazers_count,
            'forks':        repo.forks_count,
        }

        for k, v in dict(dct).items():
            if v is None:
                del dct[k]
    
    except Exception:
        dct = None

    return dct

def get_top_contributors(repo):
    c_list = []
    
    try:
        contributors = repo.get_contributors()

        for c in contributors:
            c_list.append(c.login)
            if len(c_list) >= 10:
                break
    
    except Exception:
        return []

    return c_list

def get_users_commits(name):
    usr = get_named_user(name)
    events = usr.get_events()

    commits = defaultdict(list)

    # For each event, get repo ID and commit IDs (SHAs)
    for event in events:
        repo_id = event.repo.id

        try:
            for commit in event.payload.get("commits"):
                sha = commit.get("sha")
                print(f"Found commit {sha} in repo {repo_id}")
                commits[repo_id].append(sha)
        
        except Exception:
            print("No commits in this event")

    # Should now have a dict of repo IDs and the commits the user made to each of those repos
    return commits


