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

    chinese_dict = ""
    with open('./city_pinyin_chinese.json',encoding='utf-8') as f:
        chinese_dict = f.read().strip().replace('\n',"")
        chinese_dict = json.loads(chinese_dict)
        # print(chinese_dict)
        f.close()
        # return chinese_dict

    ##############
    # print(data_clean)
    # data_clean[]
    data_return = ""
    try:
        _city = chinese_dict[data_clean['city']]
        data_clean['city_code'] = get_city_code(_city)['AREAID']
        chaos_weather = get_city_weather(data_clean['city_code'])
        data_clean['weather'] = chaos_weather
        try:
            data_clean['weather'] = str(chaos_weather).split("\=")[1]
        except:
            pass
        return data_clean
    except:
        return  "I can't get ur information via %s" % client_host



    # return data_return
    # return chinese_dict
    # print(client_host,client_port)
    # return {"ip":client_host,"port":client_port}

@app.get("/v0.5/weather/{_city_code}")
def get_city_weather(_city_code):
    #########  天气 信息获取
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
    # _city_code=101010200
    url = 'http://d1.weather.com.cn/dingzhi/%s.html'%int(_city_code) 
    print(url)                                               #   101010100
    response = requests.get(url, headers=Weather.headers, params=Weather.params, cookies=Weather.cookies, verify=False)
    response.encoding='utf-8'
    return response.text
 
 
@app.get("/v0.5/code/{_city}")
def get_city_code(_city):
    JS=''
    with open('./city.json',encoding='utf-8') as f:
        JS = f.readline()
        # print(JS)
    JS = json.loads(JS)
    _all_area={}
    for province in JS:
        for city in JS[province]:
            # _all_area.append(city)
            _all_area.update(JS[province][city])
    # return 
    # return JS
    return _all_area[_city]




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