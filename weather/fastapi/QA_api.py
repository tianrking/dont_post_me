import pandas as pd
import json 

from fastapi import Cookie, FastAPI
from typing import Optional
from fastapi import FastAPI
from fastapi import Request
import requests
from typing import List, Optional
import sys
import uvicorn
from fastapi import FastAPI,UploadFile,File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Header
import cv2
import os

# 'Access-Control-Allow-Origin'
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        print(client_host)
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




@app.get("/ip")
def get_ip(request:Request,x_token: Optional[List[str]] = Header(None),accept_encoding: Optional[str] = Header(None),user_agent: Optional[str] = Header(None),cookie: Optional[str] = Cookie(None)):
    client_host = request.client.host
    client_port = request.client.port
    return {"ip":client_host,"port":client_port,"X-Token values": x_token,"Accept-Encoding": accept_encoding,"User-Agent": user_agent,"cookie": cookie}


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

@app.post("/uploadVideo",summary="接收视频",tags=["视频处理"])
async def getFaceFeature(file: UploadFile = File(...)):
    print(f"接收视频")
    file_bytes = await file.read()  # 读取视频数据
    context = "视频文件.mp4"    # 写到本地的文件名
    with open(context,'wb') as f:   # 把视频写入文件
        f.write(file_bytes)
    # cap = cv2.VideoCapture(context)     # 读取视频数据
    # fps = cap.get(cv2.CAP_PROP_FPS)     # 统计视频的帧率
    # print('帧率 ', fps)
    # total_s = cap.get(cv2.CAP_PROP_FRAME_COUNT)     # 统计视频的帧数
    # print("帧数 = ", total_s)
    # if cap.isOpened():          # 展示视频（没有音频）
    #     while True:
    #         ok,frame = cap.read()       # 逐帧读取图像
    #         if ok:
    #             cv2.imshow('1',frame)       # 显示单帧图像
    #             cv2.waitKey(int(1000/fps-1))    # 根据帧率，延时显示下一张
    #         else:
    #             cv2.destroyAllWindows()
    #             break       # 关闭图像窗口，退出循环

    result = {'文件名':file.filename,'文件大小':sys.getsizeof(file_bytes)} # 返回接收到的视频文件的文件名和文件大小
    print(result)
    return JSONResponse(content=result)


headers = {
    'authority': 'www.jin10.com',
    'sec-ch-ua': '^\\^',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'script',
    'referer': 'https://www.jin10.com/',
    'accept-language': 'zh-TW,zh-HK;q=0.9,zh;q=0.8,en;q=0.7,zh-CN;q=0.6,en-GB;q=0.5,en-US;q=0.4',
    'cookie': 'Hm_lvt_522b01156bb16b471a7e2e6422d272ba=1645929399; sound=1; notify=2; jinSize=normal; kind_g=^%^5B^%^223^%^22^%^2C^%^227^%^22^%^5D; trend=1; x-token=; UM_distinctid=17f3909bf905e1-028195c3436eaa-a3e3164-144000-17f3909bf91a26; CNZZDATA1000171913=1230279298-1645928760-^%^7C1645928760; CNZZDATA1253039837=1625177336-1645922780-^%^7C1645922780; Hm_lpvt_522b01156bb16b471a7e2e6422d272ba=1645929551',
}

params = (
    ('t', '1645929628705'),
)

latest_msg = ""

def get_jin10_news(_n,msg_get):
   
    response = requests.get('https://www.jin10.com/flash_newest.js', headers=headers, params=params)
    clean_data = response.text.replace('var newest = ',"")[:-1]

    clean_data = json.loads(clean_data)

    for i in range (0,_n):
        msg_get.append(clean_data[i]['data']['content'])
    return msg_get
    
   
    # if latest_msg == clean_data[0]['data']['content']:
    #     pass
    # else:
    #     latest_msg = clean_data[0]['data']['content']
    #     # sned_msg = "http://127.0.0.1:5700/send_msg?user_id=973577275&message=%s" % latest_msg
    #     # sned_msg = "http://127.0.0.1:5700/send_msg?user_id=2966855301&message=%s" % latest_msg
    #     # sned_msg = "http://127.0.0.1:5700/send_msg?group_id=765096903&message=" + str(latest_msg)
    #     # sned_msg = "http://127.0.0.1:5700/send_msg?group_id=793485214&message=a" % latest_msg
    #     sned_msg = "http://127.0.0.1:5700/send_msg?group_id=971732997&message=%s" % latest_msg
        
        # print(latest_msg)
        # requests.get(sned_msg)

@app.get("/jin10/{nn}")
def get_jin10(nn):
    msg_get = []
    nn = int(nn)
    get_jin10_data = get_jin10_news(nn,msg_get)
    # print(get_jin10_data)
    return get_jin10_data
    # return json.dumps(get_jin10_data)

@app.get("/jin10")
def get_jin10_help():
    return {'get':"/jin10/number"}
