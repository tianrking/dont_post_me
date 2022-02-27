from attr import attrs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from sqlalchemy import null
import pandas as pd
from lxml import etree

#导入 ActionChains 类 模拟点击事件
from selenium.webdriver import ActionChains

options = Options()
options.headless = True
options.add_argument("--disable-notifications")
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

# read_file = pd.read_csv('相关问题.csv')
read_file = pd.read_csv('/home/tianrking/pachong/app/1微信广告帮助中心/ad_weixin_qq_com_guide_titile_clean.csv')
print(read_file.head())
# print(read_file.head())

df = read_file.copy()


# df.loc[df.shape[0]] = dict(zip(df.columns, value)
# df.iloc[]


###########
for index, row in read_file.iterrows():
    url = row['URL'] 
    print(url)
    # url = 'https://ad.weixin.qq.com/guide/175'
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # aa=soup.find(attrs={'class': 'md-panel_expanded md-panel'}).find(attrs={'class':'md-panel__header-text'})
    # df.loc[df.shape[0]]={'a':1,'b':2}
    # print(read_file.head())
    save_html="all_in_one_html_dir/"+url.split("https://ad.weixin.qq.com/guide/")[1]+".html"
    name = str(soup.find(attrs={'class': 'guide__title'}).get_text())
    
    save_html="all_in_one_html_dir/"+name+url.split("https://ad.weixin.qq.com/guide/")[1]+".html"
    print(name)
    f = open(save_html,'wb')
    f.write(driver.page_source.encode("utf-8", "ignore"))
    print("wtite %s " % save_html)
    f.close() 
    
# aa=aa.find(attrs={'class': 'md-panel__header-text'})


# url = "https://ad.weixin.qq.com/guide/" + str(165)
# driver.get(url)
# soup = BeautifulSoup(driver.page_source, 'lxml')
# time.sleep(10)
# print(soup)
# f = open("a.html",'wb')
# f.write(driver.page_source.encode("utf-8", "ignore"))
# f.close()


# url = "https://ad.weixin.qq.com/guide/" + str(165)

# url = "https://www.baidu.com"

# url = "https://ad.weixin.qq.com/guide/288"
# driver.get(url)
# time.sleep(6)
# soup = BeautifulSoup(driver.page_source, 'lxml')
# with open("a.html",'wb') as f:
#     f.write(driver.page_source.encode("utf-8", "ignore")) # 忽略非法字符
# print('写入成功')    
# print(soup)


#     print(aa.get_text())

## get_text() 
# get_text()) # 我们使用get_text()方法获得标签内容
# get['href'] # get['attrs']方法获得标签属性

# for index, row in read_file.iterrows():
#     url = row['URL'] 
#     print(url)
#     driver.get(url)
#     time.sleep(5)
#     soup = BeautifulSoup(driver.page_source, 'lxml')
#     aa=soup.find_all(attrs={'class': 'md-panel_expanded md-panel'})
#    # # html = etree.HTML(driver.page_source)
    
#     html = etree.parse(driver.page_source, etree.HTMLParser())
  #  result = html.xpath('//*')
    # result = etree.tostring(html)
    
    #html = etree.tostring(html,encoding="unicode")
    #html.xpath('//*')
   # print(html)
    # print(result.decode('utf-8'))
    
    # driver.get(url)
    # time.sleep(5)
    # soup = BeautifulSoup(driver.page_source, 'lxml')
    # aa = soup.find_all(attrs={'class': 'md-panel_expanded md-panel'})
    # print(aa) # md-panel_expanded md-panel
# url = 'https://ad.weixin.qq.com/guide/term/186'
# driver.get("https://ad.weixin.qq.com/guide/1184")

# time.sleep(5)
# soup = BeautifulSoup(driver.page_source, 'lxml')
# aa=soup.find_all(attrs={'class': 'md-panel_expanded md-panel'})
# print(aa)

# # 鼠标移动到 ac 位置
# ac = driver.find_element_by_xpath("//div[@class='md-panel__header-text']")
# ActionChains(driver).move_to_element(ac).perform()
# soup = BeautifulSoup(driver.page_source, 'lxml')
# print(soup)
# # print(soup.find(name='div'))


