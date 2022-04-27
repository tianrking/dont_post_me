# https://open.work.weixin.qq.com/help2/pc/14521?person_id=1

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from sqlalchemy import null

options = Options()
options.headless = True
options.add_argument("--disable-notifications")

options.add_argument('--headless')
options.add_argument('--disable-gpu')#谷歌文档提到需要加上这个属性来规避bug
 
options.add_argument('disable-infobars')#隐藏"Chrome正在受到自动软件的控制"
options.add_argument('lang=zh_CN.UTF-8')      # 设置中文
options.add_argument('window-size=1920x1800') # 指定浏览器分辨率
options.add_argument('--hide-scrollbars')     # 隐藏滚动条, 应对一些特殊页面
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
options.add_argument('lang=zh_CN.UTF-8')
# driver = webdriver.Chrome("/Users/mac/Desktop/chromedriver", options=options)
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

url = "https://open.work.weixin.qq.com/help2/pc/14641?person_id=1"

# mobile url way
# url = "https://open.work.weixin.qq.com/help/wap/detail?person_id=NaN&is_tencent=&docid=15545"
#
# import requests
#
# response  = requests.get(url)
# print(response.text)


driver.get(url)
driver.get_screenshot_as_file('1.png')
time.sleep(10)
print(driver.title)
driver.get_screenshot_as_file('2.png')
soup = BeautifulSoup(driver.page_source, 'lxml')

# # 4 8
# # https://open.work.weixin.qq.com/help2/pc/14207?person_id=1
# # url = "https://open.work.weixin.qq.com/help2/pc/1%s?person_id=1"%str(100)
# #url = "https://open.work.weixin.qq.com/help2/pc/14207?person_id=1"
# url = "https://open.work.weixin.qq.com/help2/pc/14207?person_id=1"
# # url = "https://www.baidu.com"
# print(url)

# driver.get(url)
# time.sleep(10)
# print(driver.title)
# soup = BeautifulSoup(driver.page_source, 'lxml')

# # print(soup)
# # aa=str(soup.find(attrs={'class': 'que_content_title'}).get_text())
    
# # print(aa)

# driver.quit()
# exit()

# # for i in range(106,3000):
# #     url = "https://ad.weixin.qq.com/guide/" + 
# #     driver.get("https://baidu.com/")
# #     print(driver.title)
# #     driver.quit()


# email = chrome.find_element_by_id("email")
# password = chrome.find_element_by_id("pass")
 
# email.send_keys(config.email)
# password.send_keys(config.password)
# password.submit()


#####
# for i in range(106,3000):
#     url = "https://ad.weixin.qq.com/guide/" + str(i)
#     driver.get(url)
#     time.sleep(5)
#     soup = BeautifulSoup(driver.page_source, 'lxml')
#     # data = driver.find_element("//meta[@name='description']")
#     # print(soup.find(name='meta')) # <meta>
#     f = open('log.txt','a')
#     if len(soup.find_all(attrs={'class': 'guide__title'})):
        
#         f.write(str(soup.find_all(attrs={'class': 'guide__title'})))
#         f.write(",")
#         f.write(url)
#         f.write('\n')
#         # f.write(soup.find_all(attrs={'class': 'guide__title'})+","+list(url)+'\n')
#         #f.close()
#     f.close() 
#     # print(soup.find_all(attrs={'class': 'guide__title'}),url)

#     # print(soup.find_all('div'))
#     # print(soup)
#     # driver.quit()

# # driver.quit()
