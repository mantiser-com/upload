import json
import requests
import os
MUATIC_AUTH= os.getenv('MUATIC_AUTH')
MUATIC_URL= os.getenv('MUATIC_URL')


header={'Authorization': 'Basic {}'.format(MUATIC_AUTH)
        ,'Content-type': 'application/json', 
        'Accept': 'application/json'}



def create_contact_mautic(emailData):
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(emailData)
    email = emailData['email'].split("@")
    data = {
        'email': emailData['email'],
        'firstname': email[0],
        'lastname': email[1],
        'website': emailData['url'],
        'tags': emailData['tech'],
        'stage': emailData['postid'],
        'owner':1
        }
    try:
        data["tags"] =emailData['tech']
    except:
        pass
    try:
        data['city'] = emailData["city"]
    except:
        pass
    try:
        data['country'] = emailData["country"]
    except:
        pass

    url = '{}/api/contacts/new'.format(MUATIC_URL)
    response = requests.request('POST', url, data=json.dumps(data), headers=header )
    print("Send to mautic")
    print(response.text)
    print(response.status_code)

    if response.status_code == 500:
        #we got a 500 lets try again without stage
        data['stage'] = 3
        response = requests.request('POST', url, data=json.dumps(data), headers=header )



def get_contacts():
    header={'Authorization': 'Basic bWFudGlzZXI6bWFudGlzZXIxMjEy', 'cache-control': "no-cache"}
    url = 'https://mautic.apps.northamlin.com/api/contacts'
    response = requests.request('GET', url, headers=header )
    print(response.text)


#create_contact_mautic("matte@elino.se","mattias","hemmingsson")    
#get_contacts()