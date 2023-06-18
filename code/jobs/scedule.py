import json
from pymongo import MongoClient
import os
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(os.getenv('MONGO_URI'))
db=client.admin
# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)
db=client.mantiser
for item in db.sources.find({"type":"2"}):
    print(item)