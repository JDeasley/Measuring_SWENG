import pymongo

# Get the user object from the db

# Establish connection
conn = "mongodb://mongo:27017"
client = pymongo.MongoClient(conn)

def main():
    # Create a database
    db = client.classDB

    print("Clearing database...")
    db.githubdata.delete_many({})

if __name__ == '__main__':
    main()
