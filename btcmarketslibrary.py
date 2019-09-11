

class BTCMarketsLibrary:

    def get_balances(self, data):

        return self.__get_active_currencies(data)

    def __get_active_currencies(self, data):
        active_currencies = {}

        for cur in data:
            if cur['balance'] == 0:
                continue
            if cur['currency'] == 'AUD':
                continue

            active_currencies[cur['currency']] = cur
            active_currencies[cur['currency']]['realBalance'] = self.__get_actual_balance(cur['balance'])

        return active_currencies

    def __get_actual_balance(self, volume):
        volume = volume / 100000000
        volume = round(volume, 2)

        return volume

    def calculate_holdings(self, current_prices, active_balances):
        for cur in active_balances:
            try:
                active_balances[cur]['total'] = round(active_balances[cur]['realBalance'] * current_prices[cur]['lastPrice'], 2)
                active_balances[cur]['lastPrice'] = current_prices[cur]['lastPrice']
            except:
                continue

        return active_balances

    def print_totals(self, holdings):
        total = 0

        print('Currency\tPrice\tQty\tTotal')
        for key, value in holdings.items():
            print("{}\t\t{}\t{}\t${}".format(key, value['lastPrice'], value['realBalance'], value['total']))
            total += value['total']

        print('Total: ${}'.format(round(total, 2)))
