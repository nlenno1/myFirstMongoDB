import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDatabase"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

# insert a new record
"""
new_doc = {"first": "douglas", "last": "adams", "dob": "11/03/1952", "hair_color": "grey", "occupation": "writer", "nationality": "british"}

coll.insert(new_doc)
"""

# insert multiple records
"""
new_docs = [{
"first": "terry",
"last": "pratchett",
"dob": "28/04/1948",
"gender": "m",
"hair_color": "not much",
"occupation": "writer",
"nationality": "british"
}, {
"first": "george",
"last": "rr martin",
"dob": "20/09/1948",
"gender": "m",
"hair_color": "white",
"occupation": "writer",
"nationality": "american"
}]

coll.insert_many(new_docs)
"""

# display all records
"""
documents = coll.find()

for doc in documents:
    print(doc)
"""

# find specific records
"""
documents = coll.find({"first": "douglas"})

for doc in documents:
    print(doc)
"""

# remove specific record
"""
coll.remove({"first": "douglas"})
"""

# update first found record
"""
coll.update_one({"nationality": "american"}, 
{"$set": {"hair_color": "maroon"}})
"""

# update all specific records
"""
coll.update_many({"nationality": "american"}, 
{"$set": {"hair_color": "maroon"}})
"""
