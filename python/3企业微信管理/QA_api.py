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

    ############## IP 与位置 信息获取
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
    response = requests.get('https://ipapi.co/%s/json/'%client_host, headers=headers)  ## 获取用户ip 地址
    data_clean = json.loads(response.text)

    ##############
    # print(data_clean)
    # return data_clean
    print(client_host,client_port)
    ##########  天气 信息获取
    class Weather:
        cookies = {
        'Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b': '1645175803,1645175814',
        'f_city': '%E5%8C%97%E4%BA%AC%7C101010100%7C',
        'Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b': '1645177503',
        }

        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
            'Accept': '*/*',
            'Referer': 'http://www.weather.com.cn/',
            'Accept-Language': 'zh-TW,zh-CN;q=0.9,zh;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,zh-HK;q=0.4',
        }

        params = (
            ('_', '1645177503970'),
        )
    
    response = requests.get('http://d1.weather.com.cn/dingzhi/101010100.html', headers=Weather.headers, params=Weather.params, cookies=Weather.cookies, verify=False)
    response.encoding='utf-8'
    return response.text




@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


## thanks https://tool.lu/curl/
## thanks https://ipapi.co/

# curl 'http://d1.weather.com.cn/sk_2d/101010100.html?_=1645175864577' \
#   -H 'Connection: keep-alive' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36' \
#   -H 'Accept: */*' \
#   -H 'Referer: http://www.weather.com.cn/' \
#   -H 'Accept-Language: zh-TW,zh-CN;q=0.9,zh;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,zh-HK;q=0.4' \
#   -H 'Cookie: Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1645175803,1645175814; f_city=%E5%8C%97%E4%BA%AC%7C101010100%7C; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1645175847' \
#   --compressed \
#   --insecure

# curl 'http://d1.weather.com.cn/dingzhi/101010100.html?_=1645177503970' \
#   -H 'Connection: keep-alive' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36' \
#   -H 'Accept: */*' \
#   -H 'Referer: http://www.weather.com.cn/' \
#   -H 'Accept-Language: zh-TW,zh-CN;q=0.9,zh;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,zh-HK;q=0.4' \
#   -H 'Cookie: Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1645175803,1645175814; f_city=%E5%8C%97%E4%BA%AC%7C101010100%7C; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1645177503' \
#   --compressed \
#   --insecure