from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb://root:passs@mongodb:27017/")
db=client.admin
# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)


def storeDB(json_data):
    '''
    Store the data into a mongodb server
    '''
    db=client.mantiser
    result=db.mantiser.insert_one(json_data)
    #Step 4: Print to the console the ObjectID of the new document
    print(' {0}'.format(result.inserted_id))