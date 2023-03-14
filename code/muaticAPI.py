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
    tags = []
    tags.append(emailData['url'])
    tags.append(emailData['postid'])
    tags.append(emailData['userid'])
    tags.append(emailData['tech'])
    tags.append(email[1])
    tags.append(emailData['prefix'])
    tags.append(emailData['projectID'])




    data = {
        'email': emailData['email'],
        'firstname': email[0],
        'lastname': email[1],
        'website': emailData['url'],
        'tags': tags,
        'stage': 3,
        'owner':1
        }
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



#testJosn =  {'email': 'reception@brohofslott.se', 'url': 'https://www.brohofslott.se//medlem', 'type': '_email', 'projectID': 'mantiser', 'userid': '1234', 'postid': '12345', 'prefix': 'none', 'dest': ['muatic'], 'tech': [], 'scannerid': '2222', 'data': {'userid': '1234', 'postid': '12345', 'scannerid': '2222', 'getemail': '2', 'project': 'mantiser', 'prefix': 'none', 'dest': ['muatic'], 'deep': 5, 'action': 'page', 'url': 'https://www.brohofslott.se/banor/the-stadium-course'}, 'timestamp': '2023-03-14T20:16:56.217137', 'id': '6410d638f5f9ef262f691d52'}
#create_contact_mautic(testJosn)
#get_contacts()