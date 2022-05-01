# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd

options = Options()
# options.headless = True
# options.add_argument("--proxy-server=socks5://127.0.0.1:12999")

# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

# driver.get("https://www.simuwang.com/")
driver.get("https://dc.simuwang.com/")  ## 私募排行

# 定位搜尋框 賬戶密碼登入
# context = driver.find_element_by_class_name("comp-login-method comp-login-b2 comp-login-active")
# 傳入字串
# context.click()
try:
    context_1 = driver.find_element(By.XPATH, value="//button[@class='comp-login-method comp-login-b2']")
    # context_1 = driver.find_element_by_xpath("//button[@class='comp-login-method comp-login-b2']")
    context_1.click()
    
    # try:
    time.sleep(2)
    username = driver.find_element_by_name('username')
    username.send_keys("15773211225")
    
    password = driver.find_element(By.XPATH, value="//input[@class='comp-login-input comp-login-user-input2']")
    password.send_keys("Lyp82nlf")
    
    login_button = driver.find_element(By.XPATH, value="//button[@class='comp-login-btn']")
    login_button.click()
    
except:
    time.sleep(2)



time.sleep(4)

from lxml import etree ## for xpath


soup = BeautifulSoup(driver.page_source, 'html.parser')


funds = soup.find_all('div', {
    'class': 'ranking-table-tbody-tr'})

# for fund in funds:
    # print(fund)
    # fund_soup = BeautifulSoup(fund, 'html.parser')
    # name = fund_soup.find('div',{'class':'ranking-table-ellipsis'})
    # dc-common-flex ranking-table-profit-tbody


page_text = driver.page_source
page_text_list = [driver.page_source]
fund_list = []
year_yield_list = []
fund_return_list = []

for source_data in page_text_list:
    dom = etree.HTML(source_data)
    # content = dom.xpath("//div[@class='ranking-table-tbody-tr']/text()")
    name = dom.xpath("//a[@class='ranking-table-link txtCut']/@title")
    one_year_return = dom.xpath("//div[@class='ranking-table-tbody-td tcenter td-focus tableActive']/p/text()")
    
    fund_list.append(name)
    fund_return_list.append(one_year_return)
    
    name_gg = dom.xpath("//div[@class='comp-common-flex aic']")
    # name_gg = dom.xpath("//div[@class='ranking-table-tbody-td tcenter td-focus']")
    # print(name_gg)
    for gg in name_gg:
        # print(gg.xpath(".//div[@class='ranking-table-tbody-td tcenter td-focus']/p/text()"))
        rr = gg.xpath(".//div[@class='ranking-table-tbody-td tcenter td-focus']/p/text()")
        # print(rr)
        fund_name = gg.xpath(".//a[@class='ranking-table-link txtCut']/@title")
        try:
            one_month = rr[0]
            three_month = rr[1]
            half_year = rr[2]
            print(fund_name,one_month,three_month,half_year)
        except:
            print("Empty")
    
    # for fund in content:s
    #     # name =  fund.xpath("/div/div[@class='ranking-table-ellipsis']")
    #     name = fund.xpath('./text()')
    #     print(name)

# for index,value in enumerate(fund_list):
#     print(value,fund_return_list[index])
    
print("w0x7ce")
print(driver.title)

# print(driver.find_elements(By.XPATH,value="//span"))
driver.quit()