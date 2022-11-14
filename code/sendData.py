import requests
import os
import json

def upload_data(json_data_in):
    '''
    Will upload data to endpoint
    '''
    # Send data to api
    print("Sedning data to API")
    #Format data to json
    #json_data= json.dumps(json_data_in)
        

    #Add keys
    #headers = {'x-api-key': os.getenv('KEY'), 'content-type': 'application/json'}
    
    #r = requests.post(os.getenv('URL'), data=json_data,  headers=headers)
    #print(r.status_code, r.reason)
    #
    #if r.status_code == 200:
    #    print("Upload complete")
    #else:
    #    print("Upload failed")
    