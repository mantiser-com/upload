import meilisearch
import json
import os 

client = meilisearch.Client(os.getenv('MEILISEARCH'),os.getenv('MEILISEARCH_KEY'))


## Bootstrap meilisearch
index = client.index('mantiser_page' )
documents = [
      { 'id': 1} ]
ret = index.add_documents(documents)

index = client.index('mantiser_email' )
documents = [
      { 'id': 1} ]
ret = index.add_documents(documents)

index = client.index('mantiser_company' )
documents = [
      { 'id': 1} ]
ret = index.add_documents(documents)

index = client.index('mantiser_people' )
documents = [
      { 'id': 1} ]
ret = index.add_documents(documents)


#except:
#  print("docs alreaddy there")
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
    # If the index 'movies' does not exist, Meilisearch creates it when you first add the documents.
    #json_data["_id"]=0
    index_add = client.index('mantiser{0}'.format(json_data['type']) )
    mreply = index_add.add_documents([json_data]) # => { "uid": 0 }
    print(mreply)