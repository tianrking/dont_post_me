import asyncio
import websockets
import json

msg = \
{
  "jsonrpc" : "2.0",
  "id" : 3601,
  "method" : "public/get_delivery_prices",
  "params" : {
    "index_name" : "btc_usd",
    "offset" : 0,
    "count" : 4
  }
}

async def call_api(msg):
   async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
       print("AAAAAA")
       await websocket.send(msg)
       while websocket.open:
           response = await websocket.recv()
           # do something with the response...
           print(response)
           print("BBBBB")

asyncio.get_event_loop().run_until_complete(call_api(json.dumps(msg)))
# print("a")
# asyncio.get_event_loop().run_until_complete(call_api(json.dumps(msg)))