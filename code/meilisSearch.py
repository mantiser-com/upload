import meilisearch
import json

client = meilisearch.Client('http://meilisearch:7700')


def addMeilsearch(json_data):
    # An index is where the documents are stored.
    print(json_data)
    user_index= "mantiser_"+str(json_data["projectID"])  #+"_"+json_data["userid"]
    
    client.create_index(user_index, {'primaryKey': 'id'})

    index = client.index(user_index)
    # If the index 'movies' does not exist, Meilisearch creates it when you first add the documents.
    #json_data["_id"]=0
    #print(json_data)
    
    index.add_documents([json_data]) # => { "uid": 0 }
    print("Data added to melissearch")