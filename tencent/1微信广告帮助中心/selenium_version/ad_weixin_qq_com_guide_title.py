from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from sqlalchemy import null


options = Options()
options.headless = True
options.add_argument("--disable-notifications")
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

# for i in range(106,3000):
#     url = "https://ad.weixin.qq.com/guide/" + 
#     driver.get("https://baidu.com/")
#     print(driver.title)
#     driver.quit()

# email = chrome.find_element_by_id("email")
# password = chrome.find_element_by_id("pass")
 
# email.send_keys(config.email)
# password.send_keys(config.password)
# password.submit()
for i in range(106,3000):
    url = "https://ad.weixin.qq.com/guide/" + str(i)
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # data = driver.find_element("//meta[@name='description']")
    # print(soup.find(name='meta')) # <meta>
    f = open('log.txt','a')
    if len(soup.find_all(attrs={'class': 'guide__title'})):
        
        f.write(str(soup.find_all(attrs={'class': 'guide__title'})))
        f.write(",")
        f.write(url)
        f.write('\n')
        # f.write(soup.find_all(attrs={'class': 'guide__title'})+","+list(url)+'\n')
        #f.close()
    f.close() 
    # print(soup.find_all(attrs={'class': 'guide__title'}),url)

    # print(soup.find_all('div'))
    # print(soup)
    # driver.quit()

# print(driver.title)
# driver.quit()
