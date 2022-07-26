import pymongo

CONNECTION_STRING = "mongodb://localhost:27017"
client = pymongo.MongoClient(CONNECTION_STRING)

db = client["botnoi"]
table = db["detail"]
