from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from sqlalchemy import null

import requests  

# url = 'https://open.work.weixin.qq.com/help2/pc/14662?person_id=1'
# r = requests.get(url)  
# print(r.text)

from tqdm import tqdm # 进度条
import requests
from bs4 import BeautifulSoup
# url = "https://open.work.weixin.qq.com/help2/pc/14662?person_id=1"



f = open("requests_url.txt",'a')
for i in tqdm(range(7636,8000)): #3000
    url = "https://open.work.weixin.qq.com/help2/pc/1%s?person_id=1"%str(i)
    # url = "https://open.work.weixin.qq.com/help2/pc/13000?person_id=1"
    res = requests.get(url,cookies = {'nothing':'1'}) # 
    Soup = BeautifulSoup(res.text,'html.parser')
    # print(Soup.title)
    print(Soup.title.text)
    # print(url)
    # f.write(str(name))
    f.write(Soup.title.text)
    f.write(",")
    f.write(url)
    f.write('\n')
f.close()
