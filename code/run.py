#
#
#
# File to start
#
# Lissen for events from the que
#!/usr/bin/env python
import asyncio
import os
import requests
import json
import asyncio
import nats
from nats.errors import TimeoutError


from sendData import upload_data
from storeMongo import storeDB
from meilisSearch import addMeilsearch
from muaticAPI import create_contact_mautic

from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)

@app.route("/ready")
def ready():
	#searchGoogle(mess['words'],mess['botid'],mess['user'],mess['email'],mess['MailChimpList'],mess['userMailChimpKey'])
	#searchGoogle(searchword,botid,userid)
	return "Move in nofing to see here !!"


'''
To test that the search adds data to nats we can use this python file
'''
async def run():

	nc = await nats.connect(os.getenv('NATS'))
	# Create JetStream context.
	js = nc.jetstream()
	
	async def message_handler(msg):
		subject = msg.subject
		reply = msg.reply
		data = msg.data.decode()
		try:
			data_json = json.loads(json.dumps(eval(data)))
			me_data_json = json.loads(json.dumps(eval(data)))
		except:
			data_json = json.loads(json.dumps(data))
			me_data_json = json.loads(json.dumps(data))
		try:
			monogid = storeDB(data_json)
			me_data_json["id"]=str(monogid)
			addMeilsearch(me_data_json)
			upload_data(data_json)
			print("%%%%%%%%%%%%%%%%%%%%")
			print(data_json['dest'])
			#If we have a email in the json upload to muatic
			if 'email' in data_json: 
				if 'muatic' in data_json['dest']:
					create_contact_mautic(data_json)
		except:
			print("Error in upload data")
			pass

	osub = await js.subscribe("upload",durable="upload")
	data = bytearray()

	while True:
		try:
			msg = await osub.next_msg()
			await message_handler(msg)
			await msg.ack()
		except TimeoutError:
			pass
			



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.run_forever()
    loop.close()

    