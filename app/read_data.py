import pymongo
import pprint
import json
from get_data import get_top_contributors

# Getting the user object from the db

# Establish connection
conn = "mongodb://mongo:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB
# data = db.githubdata.find()

def db_fetch(repo_name="folafifo/Group8OAC"):
    # with open('data.json', 'w') as f:

    top_cons = get_top_contributors(repo_name)
    top_cons_names = []

    for con in top_cons:
        top_cons_names.append(con.login)

    print("Accessing DB for users in list:")
    print(top_cons_names)
    dct = db.githubdata.find({'user': {'$in': top_cons_names}})

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
