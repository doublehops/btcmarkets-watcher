#!/usr/bin/python

from btcmarkets import BTCMarkets
import config


client = BTCMarkets (config.api_key, config.private_key)

print(client.get_account_balance())
