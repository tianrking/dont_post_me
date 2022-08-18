#wss://stream.coinmarketcap.com/price/latest

#import sleep
import time
import json
from websocket import create_connection
ws = create_connection("wss://stream.coinmarketcap.com/price/latest")
ws.send(json.dumps({"method":"subscribe","id":"price","data":{"cryptoIds":[1,1027,825,3408,1839,52,4687,2010,5426,74,6636,5994,5805,3890,4943,1958,7083,3717,1321,3957,2,4195,6535,1975,3635,3794,512,328,4558,1831,4030,2280,3077,18876,8916,1966,6210,2011,4642,6783,1765,2416,7278,3155,6892,4066,3897,2563,3602,1437,2087,5665,3330,1518,3513,16086,1720,6719,10791,4157,4256,1376,8000,19891,2502,5068,2700,7186,6538,4847,1697,1274,4705,18069,2130,131,2469,1934,2694,4846,2083,8646,5034,5567,1168,873,1659,8104,5632,3783,5964,7080,2682,7653,5692,1684,8642,2634,2586,5864,9023,9022,5824],"index":null}}))
#ws.send("id":"price")

while True:
    result =  ws.recv()
    print (result)
    time.sleep(100)

ws.close()
