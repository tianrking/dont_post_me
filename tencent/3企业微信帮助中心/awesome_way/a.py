from cmath import e
# from email import header
import requests 
import os
import json
import pandas as pd

from multiprocessing.connection import answer_challenge
from posixpath import dirname
import requests
import json
from tqdm import tqdm # 进度条
import requests
from bs4 import BeautifulSoup
import _thread 
import pandas as pd

### 可以参考
### https://tool.lu/curl/
### https://curl.6cm.co/

# curl 'https://open.work.weixin.qq.com/help2/getQusList?lang=zh_CN&ajax=1&f=json&random=310321' \
#   -H 'authority: open.work.weixin.qq.com' \
#   -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"' \
#   -H 'accept: application/json, text/plain, */*' \
#   -H 'content-type: application/json' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36 Edg/98.0.1108.51' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'origin: https://open.work.weixin.qq.com' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'referer: https://open.work.weixin.qq.com/help2/pc/15405?person_id=1' \
#   -H 'accept-language: zh-TW,zh-CN;q=0.9,zh;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,zh-HK;q=0.4' \
#   -H 'cookie: pgv_pvid=3686684000; pac_uid=0_3cbd911c9ce83; pgv_info=ssid=s2798911544; pgv_pvi=4654092288; pgv_si=s6420471808; wwrtx.ref=direct; wwrtx.c_gdpr=0; wwrtx.refid=413075501944711; __utma=114362329.896737070.1644833346.1644833346.1644833346.1; __utmc=114362329; __utmz=114362329.1644833346.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_f2ba645ba13636ba52b0234381f51cbc=1644833347; Hm_lpvt_f2ba645ba13636ba52b0234381f51cbc=1644833970; uin=o0508195902; skey=@sEUq3VJWl; RK=hA9xBYtEcN; ptcz=f4917937db9babf5c19203049471a3e4d45ea1fe7b770ef9ea93e47e33c0c0f5; wwrtx.i18n_lan=cht' \
#   --data-raw '{"person_id":1,"doc_id":15405}' \
#   --compressed

# 最简格式 ########################
#       https://open.work.weixin.qq.com/help2/getQusList?lang=zh_CN&ajax=1&f=json&random=569866
# curl 'https://open.work.weixin.qq.com/help2/getQusList?lang=zh_CN&ajax=1&f=json&random=310321' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36 Edg/98.0.1108.51' \
#   -H 'referer: https://open.work.weixin.qq.com/help2/pc/15405?person_id=1' \
#   --data-raw '{"person_id":1,"doc_id":15405}' 
####################################

# py 最简模式 ####################
# headers = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36 Edg/98.0.1108.51',
#     'referer': 'https://open.work.weixin.qq.com/help2/pc/15405?person_id=1',
# }
#
# params = (
#     ('lang', 'zh_CN'),
#     ('ajax', '1'),
#     ('f', 'json'),
# )
#
# data = '{"person_id":1,"doc_id":15405}'
#
# i=310321        
# res = requests.post('https://open.work.weixin.qq.com/help2/getQusList?random=%s' % str(i), headers=headers, params=params, data=data)
##################################################

########### 防 ban 全参数

headers = {
    'authority': 'open.work.weixin.qq.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://open.work.weixin.qq.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://open.work.weixin.qq.com/help2/pc/16526',
    'accept-language': 'zh-TW,zh-CN;q=0.9,zh;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,zh-HK;q=0.4',
    'cookie': 'pgv_pvid=3686684000; pac_uid=0_3cbd911c9ce83; pgv_pvi=4654092288; wwrtx.c_gdpr=0; __utma=114362329.896737070.1644833346.1644833346.1644833346.1; __utmz=114362329.1644833346.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_f2ba645ba13636ba52b0234381f51cbc=1644833347; RK=hA9xBYtEcN; ptcz=f4917937db9babf5c19203049471a3e4d45ea1fe7b770ef9ea93e47e33c0c0f5; wwrtx.i18n_lan=cht; pgv_info=ssid=s2791877920; pgv_si=s383571968; wwrtx.ref=direct; wwrtx.refid=6308703232183814',
}

params = (
    ('lang', 'zh_CN'),
    ('ajax', '1'),
    ('f', 'json'),
    ('random', '630161'),
)

## doc id 编号为主文档对应序号
data = '{"person_id":1,"doc_id":15405}'

## random 随机数 随意即可 不影响爬取
i=569866 # https://open.work.weixin.qq.com/help2/pc/14674?person_id=1 

# 凭爬去上两个界面的感觉 有效条目在两千一下 大概率在五百到一千之间
# 数值范围可以给大一些 从13000 到 18000 分五次爬取
# 因为存在连续抓取被服务器 ban 的可能 这块没有实现自动化 
# 多线程 五次也是很快的 每次检查数据再下一次抓取

# 15000-16000 1k
# 16000-17000 2k
# 17000-18000 3k
# 18000-19000 4k
# 19000-20000 5k
# 14000-15000 6k

def request_api(T_name,begin,end):
    df = pd.DataFrame()

    for i in tqdm(range(begin,end)):
        
        data = '{"person_id":1,"doc_id":%s}'% str(i)                   
        res = requests.post('https://open.work.weixin.qq.com/help2/getQusList', headers=headers, params=params, data=data)

        res = json.loads(res.text)
        # print(res['data'])
        # print(res)
        # f = open('aaaaa.json','w')
        # f.write(str(res))
        # f.close()
        # exit()
        
        try:
            Q = res['data']['helpdocument']['qusList'][0]['title']
            print(i)
            A_md = res['data']['helpdocument']['qusList'][0]['content_md']
            A_URL = "https://open.work.weixin.qq.com/help2/pc/16652/"+str(res['data']['helpdocument']['id'])
            
            print("ABC")
            # A_html = res['data']['helpdocument']['qusList'][0]['content_html']
            # A_txt = res['data']['helpdocument']['qusList'][0]['content_txt']
            df = pd.DataFrame(data=[
                    [Q,A_md,A_URL]],
                    columns = ['Q','A','URL'],
                    )
            df.to_csv('data_all_in_one/QA_7k.csv', mode='a', header=False)
            
        except:
            continue
        # print(i,Q)
        # print(A_md[:20])
        
try:
    begin = 13000
# 15000-16000 1k  # 16000-17000 2k # 17000-18000 3k # 18000-19000 4k
# 19000-20000 5k # 14000-15000 6k $ 13000-14000 7k
    end = 14000
    sum = end - begin
    step = 4
    time = int(sum / step)
    _thread.start_new_thread(request_api, ("Thread-1", 0+begin , begin+time) )
    _thread.start_new_thread(request_api, ("Thread-2", begin + time , begin + time*2) )
    _thread.start_new_thread(request_api, ("Thread-3", begin + time*2 , begin + time*3) ) 
    _thread.start_new_thread(request_api, ("Thread-4", begin + time*3,  begin + time*4) )
    # _thread.start_new_thread(download, ("Thread-5", start , k , 3) )
except:
   print ("Error: 无法启动线程")


while 1:
    pass        

