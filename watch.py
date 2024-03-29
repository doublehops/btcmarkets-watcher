#!/usr/bin/python

#########################################################
##
## This script will pull your holdings from BTCMarkets
## and print the totals to the screen.
##
#########################################################

from btcmarketsconn import BTCMarketsConn
from btcmarketslibrary import BTCMarketsLibrary
import config


client = BTCMarketsConn(config.api_key, config.private_key)
btcmlib = BTCMarketsLibrary()

balances = client.get_account_balance()
active_balances = btcmlib.get_balances(balances)
current_prices = client.get_current_prices(active_balances.keys())
holdings = btcmlib.calculate_holdings(current_prices, active_balances)

btcmlib.print_totals(holdings)
