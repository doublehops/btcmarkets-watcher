#!/usr/bin/python

from btcmarkets import BTCMarkets
import config


client = BTCMarkets (config.api_key, config.private_key)

data = client.get_account_balance()
#print(data)

for cur in data:
    if cur['balance'] != 0:
        print(cur['currency'] +': '+ str(cur['balance']))
