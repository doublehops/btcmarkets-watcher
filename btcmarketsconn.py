import base64, hashlib, hmac, urllib, urllib.request, time, urllib, json
from collections import OrderedDict

class BTCMarketsConn:

    base_url = 'https://api.btcmarkets.net'

    def __init__(self, key, secret):

        self.key = key
        self.secret = base64.b64decode(secret)


    def build_signature(self, path, secret, nowInMilliseconds):

        stringToSign = path + "\n" + nowInMilliseconds + "\n"
        hm = hmac.new(secret, stringToSign.encode("utf-8"), hashlib.sha512).digest()
        signature = base64.b64encode(hm)

        return signature


    def make_request(self, path):

        timestamp = nowInMilliseconds = str(int(time.time() * 1000))
        signature = self.build_signature(path, self.secret, nowInMilliseconds)

        headers = {
            'accept': 'application/json', 
            'Content-Type': 'application/json',
            'User-Agent': 'btc markets python client',
            'accept-charset': 'utf-8',  
            'apikey': self.key,
            'signature': signature,
            'timestamp': timestamp,
        }

        request = urllib.request.Request(self.base_url + path, headers = headers)
        response = urllib.request.urlopen(request)

        return json.load(response)


    def get_account_balance(self):

        return self.make_request("/account/balance")

    def get_current_prices(self, currencies):

        current_prices = {}

        for cur in currencies:
            currency = self.make_request("/market/"+ cur +"/AUD/tick")
            current_prices[cur] = currency

        return current_prices
