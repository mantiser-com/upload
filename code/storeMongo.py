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


    if mongo_data['type'] == "_company":
        result=db.result_company.insert_one(mongo_data)
        #Step 4: Print to the console the ObjectID of the new document
        print(' {0}'.format(result.inserted_id))
        return result.inserted_id
    elif mongo_data['type'] == "_page":
        result=db.result_page.insert_one(mongo_data)
        #Step 4: Print to the console the ObjectID of the new document
        print(' {0}'.format(result.inserted_id))
        return result.inserted_id
    elif mongo_data['type'] == "_people":
        result=db.result_person.insert_one(mongo_data)
        #Step 4: Print to the console the ObjectID of the new document
        print(' {0}'.format(result.inserted_id))
        return result.inserted_id
    elif mongo_data['type'] == "_email":
        result=db.result_email.insert_one(mongo_data)
        #Step 4: Print to the console the ObjectID of the new document
        print(' {0}'.format(result.inserted_id))
        return result.inserted_id
    elif mongo_data['type'] == "_watch":
        result=db.result_watch.insert_one(mongo_data)
        #Step 4: Print to the console the ObjectID of the new document
        print(' {0}'.format(result.inserted_id))
        return result.inserted_id
    elif mongo_data['type'] == "_car":
        result=db.result_car.update_one({'_id':mongo_data['id']}, {'$set':mongo_data},upsert=True)
        #Step 4: Print to the console the ObjectID of the new document
        print(' {0}'.format(result.upserted_id))
        return result.upserted_id

    else:
        result=db.result_other.insert_one(mongo_data)
        #Step 4: Print to the console the ObjectID of the new document
        print(' {0}'.format(result.inserted_id))
        return result.inserted_id