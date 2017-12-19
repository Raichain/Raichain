from chain.model.chain import SearchChain 
import requests
import json

def get_peers():
	command = '{ "action": "peers" }'
	search = SearchChain(command)
	return search.info

def withoutPort(ip):
	without_port = []
	ip = ip.split('.')
	for i in range(4):
		if i < 3:
			without_port.append(ip[i])
		elif i == 3:
			without_port.append(ip[i].split(':')[0])

	return '.'.join(without_port)
