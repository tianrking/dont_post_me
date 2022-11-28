import asyncio
import websockets
import json

msg = \
{
  "jsonrpc" : "2.0",
  "id" : 9929,
  "method" : "public/auth",
  "params" : {
    "grant_type" : "client_credentials",
    "client_id" : "OvgVuMCZ",
    "client_secret" : "Q3lsuXXpSu5vl7iy9dTHbScb9HRv7rRfyteQhZUaxZg"
  }
}

async def call_api(msg):
   async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
       await websocket.send(msg)
       while websocket.open:
           response = await websocket.recv()
           # do something with the response...
           print(response)

asyncio.get_event_loop().run_until_complete(call_api(json.dumps(msg)))