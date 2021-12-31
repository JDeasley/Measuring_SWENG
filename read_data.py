import pymongo
import pprint
import json
from get_data import get_top_contributors

# Getting the user object from the db

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB
# data = db.githubdata.find()

def db_fetch(repo_name="folafifo/Group8OAC"):
    # with open('data.json', 'w') as f:

    top_cons = get_top_contributors(repo_name)

    print("Accessing DB...")
    dct = db.githubdata.find({'user': {'$in': top_cons}})

    print("Done:")
    # pprint.pprint(dct)

    u_list = []

    for user in dct:
        name = user['user']
        files = user['files']

        new = {
            "user": name,
            "files": files
        }
        u_list.append(new)

    # if u_list:
    #     json.dump(u_list, f)

    return u_list

def main():
    print(db_fetch())

if __name__ == '__main__':
    main()
