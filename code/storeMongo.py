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


def storeDB(mongo_data):
    '''
    Store the data into a mongodb server
    '''
    db=client.mantiser
    #userid=json_data["userid"]
    collection = 'results{0}'.format(mongo_data['type'])
    result=db.mantiser.collection.insert_one(mongo_data)
    #Step 4: Print to the console the ObjectID of the new document
    print(' {0}'.format(result.inserted_id))
    return result.inserted_id