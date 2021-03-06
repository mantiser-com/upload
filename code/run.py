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
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

from sendData import upload_data
from storeMongo import storeDB

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
async def run(loop):
	nc = NATS()
	await nc.connect("{}:4222".format(os.getenv('NATS')), loop=loop)
	async def message_handler(msg):
		subject = msg.subject
		reply = msg.reply
		data = msg.data.decode()
		data_json = json.loads(json.dumps(eval(data)))
		print(data_json)
		storeDB(data_json)
		upload_data(data_json)
	# Simple publisher and async subscriber via coroutine.
	
	sid = await nc.subscribe("upload", cb=message_handler)
	print("Connected to nats waith response")





if __name__ == '__main__':
    #app.run(debug=True)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.run_forever()
    