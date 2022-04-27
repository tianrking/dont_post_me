
from multiprocessing.connection import answer_challenge
from posixpath import dirname
import requests
import json
from tqdm import tqdm # 进度条
import requests
from bs4 import BeautifulSoup
import _thread 
import pandas as pd


def request_api(T_name,begin,end):
    df = pd.DataFrame()
    for i in tqdm(range(begin,end)):
        # i = 1712
        url = 'https://e.qq.com/portal/helper/contents?post_id=%s' % str(i) #1712
        res = requests.get(url,cookies = {'nothing':'1'}) # 
        Soup = BeautifulSoup(res.text,'html.parser')
        JS = json.loads(res.text)
        # print(Soup.text.title)
        # print(JS)
        if JS['code']!=0:
            continue
        if JS['code']==0:
            question = JS['data']['title'] # 问题
            answer = JS['data']['content'] # 文字答案
            cid = JS['data']['catalogs'][0]['catalog_id'] # cid URL 参数
            pid = JS['data']['post_id'] # pid URL 参数
            update = JS['data']['updated_at'] # 更新时间
            # https://e.qq.com/ads/helpcenter/detail?cid=576&pid=1712
            url = "https://e.qq.com/ads/helpcenter/detail?cid=%s&pid=%s" % (str(cid),str(pid))
            
            dir = 'data_all_in_one/'
            dirname = dir + "QA"+'.txt'
            write_data = question+',' + answer + "\n"
            # f = open(dirname,'a')
            # f.write(write_data)
            # f.close()
            df = pd.DataFrame(data=[
                [question,answer,url,update]],
                columns = ['Q','A','URL','update'],
                )
            # df = 
            df.to_csv('data_all_in_one_with_url/QA_7k.csv', mode='a', header=False)
            print(url)
            
        # print(T_name)
        # print(i)
try:
    begin = 7000  
    # 1000-2000 1k # 2000-3000 2k 0 ? # 3000-4000 3k # 4000-5000 4k # 5000-6000 5k 
    # 6000-7000 6k # 7000-8000 7k
    end = 8000
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

