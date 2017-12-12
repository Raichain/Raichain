import json
import pycurl
from io import BytesIO

class SearchChain:

	def __init__(self, command):
		
		buffer = BytesIO()
		c = pycurl.Curl()
		c.setopt(c.URL, '127.0.0.1')
		c.setopt(c.PORT, 7076)
		c.setopt(c.POSTFIELDS, json.dumps(command))
		c.setopt(c.WRITEFUNCTION, buffer.write)
		output = c.perform()
		c.close()

		body = buffer.getvalue()
		info = json.loads(body.decode('iso-8859-1'))

		self.info = info 

