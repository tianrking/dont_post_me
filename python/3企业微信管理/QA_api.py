import pandas as pd
import json 

from typing import Optional
from fastapi import FastAPI
from fastapi import Request
import requests

app = FastAPI()

@app.get("/")
def return_hello(request:Request):
    client_host = request.client.host
    client_port = request.client.port

    headers = {
        'authority': 'ipapi.co',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://ipapi.co/',
        'accept-language': 'zh-TW,zh-CN;q=0.9,zh;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,zh-HK;q=0.4',
        'cookie': 'csrftoken=FdGeqPwLjImLD0UiXlTmU9e9owweqlB1b5QNITlecSISbZd8h2jAABMG5YFpHq2b',
    }
    # client_host ="111.11.11.1"
    response = requests.get('https://ipapi.co/%s/json/'%client_host, headers=headers)
    # data_clean = json.loads(response.text)
    # print(data_clean)
    return response.text

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}