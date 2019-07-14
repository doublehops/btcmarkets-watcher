

class BTCMarketsLibrary:

    def get_balances(self, data):

        active_currencies = self.get_active_currencies(data)

        return active_currencies

    def get_active_currencies(self, data):
        
        active_currencies = {}

        for cur in data:
            if cur['balance'] != 0:
                active_currencies[cur['currency']] = cur
                active_currencies[cur['currency']]['realBalance'] = self.get_actual_balance(cur['balance'])

        return active_currencies

    def get_actual_balance(self, volume):

        volume = volume / 100000000
        volume = round(volume, 2)

        return volume

    def calculate_holdings(self, current_prices, active_balances):

        total = 0

        for cur in active_balances:
            try:
                active_balances[cur]['total'] = round(active_balances[cur]['realBalance'] * current_prices[cur]['bestBid'], 2)
                active_balances[cur]['lastPrice'] = current_prices[cur]['lastPrice']
                total += active_balances[cur]['total']
            except:
                continue

        return active_balances

