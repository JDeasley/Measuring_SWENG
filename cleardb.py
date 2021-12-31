import pymongo

# Get the user object from the db

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

db.githubdata.delete_many({})