import pymongo
import pprint
import json

# Getting the user object from the db

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB
# data = db.githubdata.find()

with open('data.json', 'w') as f:
    print("Accessing DB...")
    dct = db.githubdata.find()

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

    if u_list:
        json.dump(u_list, f)