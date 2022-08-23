import meilisearch
import json
import os 

client = meilisearch.Client(os.getenv('MEILISEARCH'))


## Bootstrap meilisearch
index = client.index('mantiser_page')
documents = [
      { 'userid': 1, 'postid': 1, 'h1': ['data', 'data'] }]

ret = index.add_documents(documents)
print(ret)

try: 
  filter = client.index('mantiser_page').update_filterable_attributes([
    'userid',
    'postid',
    'h1'
  ])
except:
  print("Error setting filter on index")

try: 
  sort = client.index('mantiser_page').update_sortable_attributes([
    'scantime',

  ])
except:
  print("Error setting sort on index")




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