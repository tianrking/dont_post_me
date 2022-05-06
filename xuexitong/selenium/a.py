# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.headless = True
# options.add_argument("--proxy-server=socks5://127.0.0.1:12999")

# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

driver.get("https://i.chaoxing.com/")
time.sleep(1)
driver.save_screenshot("login.png")
element = driver.find_element(By.ID, value="quickCode")
# print(element.location) 
# {'x': 706, 'y': 252
# print(element.size) 
# {'height': 180, 'width': 180}
left = element.location['x']
right = element.location['x'] + element.size['width']
top = element.location['y']
bottom = element.location['y'] + element.size['height']

img = Image.open("login.png")
img = img.crop((left,top,right,bottom))
# img.save("login_crop.png")
  
# pip install pillow qrcode
#  pip install qrcode-terminal
# pip install pyzbar
# sudo apt-get install zbar-tools

from PIL import Image
import pyzbar.pyzbar as pyzbar

# img_path = 'login_crop.png'
# img = Image.open(img_path)

#使用pyzbar解析二维码图片内容
barcodes = pyzbar.decode(img)

#打印解析结果，从结果上可以看出，data是识别到的二维码内容，rect是二维码所在的位置
# print(barcodes)
# [Decoded(data=b'http://www.h3blog.com', type='QRCODE', rect=Rect(left=7, top=7, width=244, height=244), polygon=[Point(x=7, y=7), Point(x=7, y=251), Point(x=251, y=251), Point(x=251, y=7)])]

import qrcode_terminal
for barcode in barcodes:
    barcode_content = barcode.data.decode('utf-8') # 二维码内容
    # print(barcode_content)
    # barcode_rect = barcode.rect # 二维码在图片中的位置
    # qr_size = list(barcode_rect) #二维码大小
    # print(qr_size)
    qrcode_terminal.draw(barcode_content)





# print(i)