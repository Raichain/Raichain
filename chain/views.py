# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from chain.model.wallet_info import *
from chain.model.block_info import *
from django.shortcuts import render
import json

def index(request):
	return render(request, 'index.html')

def wallet(request):
	address = request.GET.get('w')
	wallet = Wallet(address)
	if wallet.error:
		return render(request, 'wallet.html', {'error':wallet.error})	
	else:
		transactions = wallet.transactions()
		return render(request, 'wallet.html', {'address':address, 'balance':wallet.balance, 'blockcount':wallet.blockCount, 'transactions':transactions})

def block(request):
	block_hash = request.GET.get('b')
	block = Block(block_hash)
	b = json.loads(block.get_info()['contents'])

	return render(request, 'block.html', {'binfo':b, 'block_hash':block_hash, 'account':block.account})