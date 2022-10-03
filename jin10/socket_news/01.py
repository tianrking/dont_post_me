
# pip install websocket-client
import websocket
uri = "wss://b-price.jin10.com/"
ws = websocket.create_connection(uri, timeout=10)
message1 = "Eye4CwAABwAMAFhBVVVTRC5HT09EUwwAWEFHVVNELkdPT0RTCwBVS09JTC5HT09EUwsAVVNPSUwuR09PRFMHAERYWS5OWUYKAEVVUlVTRC5OWSQJAGFnODg4LlNIRg=="
ws.send(message1)
# ws.send(message2)
while True:
    ws.send("")
    try:
        result = ws.recv()
        # print(result.decode("utf-8"))
        print(str(result,'UTF-8'))
    except:
        result = ws.recv()
        print(result)
