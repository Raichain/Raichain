from chain.model.chain import SearchChain 
from chain.model.rai_raw import raw_rai

class Wallet:

	def __init__(self, address):
		command = '{"action": "account_info", "account": "%s"}' %address
	
		search = SearchChain(command)
		self.address = address
		self.error = False;
		self.openBlock = search.info['open_block']
		self.frontier = search.info['frontier']
		self.representativeBlock = search.info['representative_block']
		self.balance = raw_rai(search.info['balance'])
		self.blockCount = search.info['block_count']

	def transactions(self):
		command = '{ "action": "account_history", "account": "%s", "count": "10"}' %self.address
		transactions = SearchChain(command)
		print(transactions.info)
		return transactions.info['history']

	
