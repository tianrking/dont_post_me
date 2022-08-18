from websocket import create_connection

ws = create_connection("wss://stream.coinmarketcap.com/price/latest/")
print(ws.recv())
print("Sending 'Hello, World'...")
ws.send("Hello, World")
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()
