import json
import requests

class SearchChain:

	def __init__(self, command):
		
		r = requests.post('http://127.0.0.1:7076', data=command)
		info = json.loads(r.text)

		self.info = info 

