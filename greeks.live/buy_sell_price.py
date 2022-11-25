
# wss://www.deribit.com/ws/api/v2
# {"id":1007,"method":"public/subscribe","params":{"channels":["trades.ETH-PERPETUAL.100ms"]},"jsonrpc":"2.0"}

import json
import websocket  
import gzip

CHANNELS_WS = [
    # 这里输入需要订阅的频道
]

class Feed(object):

    def __init__(self,url) -> None:
        self.url = url      # 这里输入websocket的url
        self.ws = None
    
    def on_open(self,sub_param) -> None:
    

        # 开始订阅
        self.sub_param = sub_param
        self.sub_str = json.dumps(self.sub_param)
        print("Following Channels are subscribed!")
        print(CHANNELS_WS)
    
    def on_url(self) -> None:
        
        self.ws = websocket.create_connection(self.url, 2) 
    
    def on_sub(self) -> None:
        
        self.ws.send(self.sub_str)
        
    def on_get_recv(self) -> str:
        
        oriData=self.ws.recv() 
        # result=gzip.decompress(oriData).decode('utf-8')
        # return result
        return oriData
    
# {"jsonrpc":"2.0","method":"subscription","params":{"channel":"trades.ETH-PERPETUAL.100ms","data":[{"trade_seq":112830104,"trade_id":"ETH-153702635","timestamp":1669360427665,"tick_direction":0,"price":1180.15,"mark_price":1180.19,"instrument_name":"ETH-PERPETUAL","index_price":1180.53,"direction":"buy","amount":30.0}]}}


req_data  = {"id":1007,"method":"public/subscribe","params":{"channels":["trades.ETH-PERPETUAL.100ms"]},"jsonrpc":"2.0"}

gg = Feed("wss://www.deribit.com/ws/api/v2")
gg.on_open(req_data)
gg.on_url()
gg.on_sub()
while True:
    
    try:
        
        data = json.loads(gg.on_get_recv())
        print(data["params"]['data'])
        
    except:
        print("GGGGGGGGGGGGGGGGG")
        pass