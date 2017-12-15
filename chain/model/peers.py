from chain.model.chain import SearchChain 

def get_peers():
	command = '{ "action": "peers" }'
	search = SearchChain(command)
	return search.info