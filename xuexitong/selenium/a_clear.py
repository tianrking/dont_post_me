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

from PIL import Image
import pyzbar.pyzbar as pyzbar

barcodes = pyzbar.decode(img)

import qrcode_terminal
for barcode in barcodes:
    barcode_content = barcode.data.decode('utf-8') # 二维码内容
    qrcode_terminal.draw(barcode_content)
