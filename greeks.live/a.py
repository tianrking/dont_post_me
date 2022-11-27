import requests
import json
import time

class Trader:
    
    def __init__(self) -> None:
        
        pass
        
        # self.isRun = True
        # self.maxPositiveCoinDelta = 1,
        # self.maxNegativeCoinDelta = 1,
        # self.maxPositiveUsdDelta = 1000,
        # self.maxNegativeUsdDelta = 1000,
        # self.positiveHedgeRatio = 100,
        # self.negativeHedgeRatio = 100,
        # self.coinTargetDelta = 0,
        # self.usdTargetDelta = 0,
        # self.eachOrderSize = 2,
        # self.makerEachOrderSize = 20,
        # self.longFuture = 'ETH-PERPETUAL',
        # self.shortFuture = 'ETH-PERPETUAL',
        # self.coinDeltaMode = False,
        # self.orderType = 'taker',  
    
    def set_cookies(self,cookie_value) -> None:
        
        self.cookies = cookie_value
        
        
    def set_headers(self,headers_value) -> None:
        
        self.headers = headers_value
        
    def get_edit_url(self,number = 1) -> str:
        
        if number == 1:
            
            return "https://www.greeks.live/ddh/strategy/edit"
        
    def set_eth_edit_url(self,eth_url) -> None:
        
        self.eth_edit_url = eth_url
        
        
    def set_json_data(self,json_data) -> str:
        
        self.json_data = json_data
        
    def change(self) -> str:
        
        return requests.post(self.eth_edit_url, cookies=self.cookies, headers=self.headers, json=self.json_data)
    
    def get_eth_now_price(self,crypto_pair = "eth_usd") -> str:
        
        requests_url = "https://test.deribit.com/api/v2/public/get_index_price?index_name=%s" % str(crypto_pair)
        self.eth_price = requests.get(requests_url)
        return self.eth_price.text
    
    def set_eth_gap(self, _gap=50 ) -> None:
        
        self.gap = _gap
        
    def get_eth_gap(self, _gap=50 ) -> int:
        
        return self.gap
        
    def set_eth_price_high(self, eth_price_high = 1500 ) -> None:
    
        self.eth_price_high = eth_price_high
    
    def set_eth_price_low(self, eth_price_low = 1000 ) -> None:
    
        self.eth_price_low = eth_price_low
        
    def get_eth_price_range(self) -> (int,int):
        
        return self.eth_price_low,self.eth_price_high
        
    
cookies = {
    'ph_phc_UlbOZqDIVLNVC2uoyTfUBMZ2gGvjUOc1fG9xHTKCbjZ_posthog': '%7B%22distinct_id%22%3A%22266545%22%2C%22%24device_id%22%3A%22184a9651f8a94e-0558faaedec802-7d5d5471-144000-184a9651f8b16fc%22%2C%22%24user_id%22%3A%22266545%22%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fgreeks.live%2F%22%2C%22%24initial_referring_domain%22%3A%22greeks.live%22%2C%22%24referrer%22%3A%22https%3A%2F%2Fgreeks.live%2F%22%2C%22%24referring_domain%22%3A%22greeks.live%22%2C%22%24sesid%22%3A%5B1669289287564%2C%22184a9651e80172c-02feb6c927e662-7d5d5471-144000-184a9651e811bf8%22%2C1669289287296%5D%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%7D%7D',
    'session': 'eyJrZXkiOiJ2eGZCUnJ0aSJ9.Y39aGw.NyYcdENpsmeB3YvsyEh26WfOfGU',
    'lang': 'zh',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'ph_phc_UlbOZqDIVLNVC2uoyTfUBMZ2gGvjUOc1fG9xHTKCbjZ_posthog=%7B%22distinct_id%22%3A%22266545%22%2C%22%24device_id%22%3A%22184a9651f8a94e-0558faaedec802-7d5d5471-144000-184a9651f8b16fc%22%2C%22%24user_id%22%3A%22266545%22%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fgreeks.live%2F%22%2C%22%24initial_referring_domain%22%3A%22greeks.live%22%2C%22%24referrer%22%3A%22https%3A%2F%2Fgreeks.live%2F%22%2C%22%24referring_domain%22%3A%22greeks.live%22%2C%22%24sesid%22%3A%5B1669289287564%2C%22184a9651e80172c-02feb6c927e662-7d5d5471-144000-184a9651e811bf8%22%2C1669289287296%5D%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%7D%7D; session=eyJrZXkiOiJ2eGZCUnJ0aSJ9.Y39aGw.NyYcdENpsmeB3YvsyEh26WfOfGU; lang=zh',
    'Origin': 'https://www.greeks.live',
    'Referer': 'https://www.greeks.live/ddh/strategy/list',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

def set_payload(_status,_usdTargetDelta = 1,_eachOrderSize=2) -> str:
    
    json_data = {
        'type': 'AdvancedDynamicDeltaStrategy',
        'curr': 'ETH',
        'subId': 266545,
        'param': {
            'isRun': True,
            'maxPositiveCoinDelta': 1,
            'maxNegativeCoinDelta': 1,
            'maxPositiveUsdDelta': 1000,
            'maxNegativeUsdDelta': 1000,
            'positiveHedgeRatio': 100,
            'negativeHedgeRatio': 100,
            'coinTargetDelta': 0,
            'usdTargetDelta': _usdTargetDelta,
            'eachOrderSize': _eachOrderSize,
            'makerEachOrderSize': 20,
            'longFuture': 'ETH-PERPETUAL',
            'shortFuture': 'ETH-PERPETUAL',
            'coinDeltaMode': False,
            'orderType': 'taker',
        },
    }
    return json_data


test_class = Trader()
test_class.set_cookies(cookies)
json_data = set_payload(False,0,_eachOrderSize=2)
test_class.set_json_data(json_data)
test_class.set_headers(headers)
test_class.set_eth_edit_url('https://www.greeks.live/ddh/strategy/edit')
test_class.set_eth_gap()
test_class.set_eth_price_high()
test_class.set_eth_price_low()

flag = 0

while True:
    
    cost = test_class.get_eth_now_price() 
    cost = json.loads(cost)['result']['index_price']
    cost = float(cost)
    
    eth_gap = test_class.get_eth_gap()
    eth_low_price , eth_high_price = test_class.get_eth_price_range()
    
    if float(eth_high_price + eth_gap) < cost:
        
        if flag != 2:
            json_data = set_payload(True,-10,_eachOrderSize=2)
            test_class.set_json_data(json_data)
            flag = 2
        
        
        print(eth_high_price + eth_gap)
        
    elif float(eth_low_price - eth_gap) > cost:
        
        if flag !=  3:
            json_data = set_payload(True,10,_eachOrderSize=2)
            test_class.set_json_data(json_data)
            flag = 3
        
        print(eth_low_price - eth_gap)

    else :
        
        if flag !=  1:
            json_data = set_payload(True,0,_eachOrderSize=2)
            test_class.set_json_data(json_data)
            flag = 1
        
        print(cost)

    print(time.asctime(time.localtime(time.time())))