from chain.model.chain import *

def raw_rai(value):
	command = '{ "action": "rai_from_raw", "amount": %s }' %value
	result = SearchChain(command)

	return result.info['amount']