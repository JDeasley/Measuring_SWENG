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

# with open('data.json', 'w') as f:
    # f.write('User,Count\n')
print("Accessing DB...")
dct = db.githubdata.find()

print("Done:")
# pprint.pprint(dct)

for user in dct:
    pprint.pprint(user)
    print()
        # f.write(user['user'] + ',' + str(user['public_repos']) + '\n')
