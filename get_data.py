from github import Github
import os
import pymongo

from collections import defaultdict

token = os.getenv('GITHUB_PAT')
g = Github(token)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.classDB

not_useful_extensions = ["class", "md", "png", "PNG", "jpg", "JPG", "jpeg", "svg", "gif", "ico"]
users_fetched = []

def get_named_user(name):
    try:
        usr = g.get_user(name)
    except Exception:
        usr = None

    return usr

def get_named_repo(repo_name):
    try:
        repo = g.get_repo(repo_name)
    except Exception:
        repo = None

    return repo

def get_top_contributors(repo_name):
    repo = get_named_repo(repo_name)
    c_list = []
    
    try:
        contributors = repo.get_contributors()
        print("Top 5 contributors:")

        for c in contributors:
            print(c.login)
            c_list.append(c)
            if len(c_list) >= 5:
                break
    
    except Exception as err:
        raise err

    return c_list

def get_users_commits(user):
    events = user.get_events()

    commits = defaultdict(list)

    # For each event, get repo ID and commit IDs (SHAs)
    for event in events:
        if event.type == "PushEvent":
            repo_id = event.repo.id

            try:
                for commit in event.payload.get("commits"):
                    sha = commit.get("sha")
                    # print(f"Found commit {sha} in repo {repo_id}")
                    commits[repo_id].append(sha)
            
            except Exception as err:
                raise err
        else:
            continue

    # Should now have a dict of repo IDs and the commits the user made to each of those repos
    return commits

def get_user_file_count(user):
    commits = get_users_commits(user)
    file_count = defaultdict(int)

    print("\nGetting files committed by user", user.login, "to repos:")

    for repo_id in commits.keys():
        try:
            repo = get_named_repo(repo_id)
            print(repo.full_name)

            for commit_id in commits.get(repo_id):
                commit = repo.get_commit(commit_id)
                
                for file in commit.files:
                    try:
                        _, file_type = os.path.splitext(file.filename)
                        file_type = file_type.removeprefix(".")
                        
                    except Exception:
                        print("Issue with file - ", file.filename, " - in repo - ", repo.full_name)
                        _, _, file_type = file.filename.split(".")
                        
                    if not file_type == '' and not file_type in not_useful_extensions:
                        file_count[file_type] += 1

        except Exception as e:
            print("Repo: ", repo_id, " - ", e)

    return file_count


def fetch(repo_name="JDeasley/Measuring_SWENG_Visualisation"):
    print("Starting 'fetch' function...")#

    try:
        top_cons = get_top_contributors(repo_name)
    except Exception as err:
        raise err

    for c in top_cons:

        if c.login not in users_fetched:
            dct = {
                'user':     c.login,
                'files':    get_user_file_count(c)
            }
            print(dct)
        
            users_fetched.append(c.login)
            db.githubdata.insert_many([dct])
        else:
            print("Already fetched file count for: ", c.login)
    
def main():
    fetch()

if __name__ == '__main__':
    main()

