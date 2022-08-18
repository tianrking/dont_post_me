import requests

headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://coinmarketcap.com',
    'Accept-Language': 'en-US,en;q=0.9',
    'Sec-WebSocket-Key': 'LeYxXPzuPUspWASbXBND2A==',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.44',
    'Upgrade': 'websocket',
    'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
    'Cache-Control': 'no-cache',
    'Connection': 'Upgrade',
    'Sec-WebSocket-Version': '13',
}

response = requests.get('http://stream.coinmarketcap.com/price/latest', headers=headers)
print(response.text())
