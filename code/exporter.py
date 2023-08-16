import json
from pymongo import MongoClient
import os
# pprint library is used to make the output look more pretty
from pprint import pprint
import csv
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(os.getenv('MONGO_URI'))
db=client.mantiser
# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)


def cars():
    f = open("results.json", "a")
    result=db.result_car.find()
    f.write("[")
    for doc in result:
        f.write(json.dumps(doc)+",\n")

    f.write("]")


def convertJsonToExcel():
    with open('results.json') as json_file:
        jsondata = json.load(json_file)
    
    data_file = open('jsonoutput.csv', 'w', newline='')
    csv_writer = csv.writer(data_file)
    
    count = 0
    for data in jsondata:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
    
    data_file.close()
    

#cars()
convertJsonToExcel()