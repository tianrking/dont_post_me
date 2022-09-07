# playwright codegen https://www.tianyancha.com --load-storage cookie_login
# playwright codegen https://www.tianyancha.com --save-storage cookie_login

from contextlib import nullcontext
from time import sleep
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import pandas as pd

class tianyan_vc:
    
    # 产品名称	所属公司	参与轮次	投资时间	投资金额	产品介绍
    
    company_name = ""
    company_full_name = ""
    
    company_vc_agency = ""
    company_investment_amount = "" 
    company_investment_time = ""
    company_vc_state = ""

    company_describe = ""     
    URL = ""  
    

def run(playwright: Playwright) -> None:
    
    # Python
    proxy_to_use = {
        'server': '123.123.123.123:80'
    }

    browser = playwright.chromium.launch(headless=True) # proxy=proxy_to_use,
    context = browser.new_context(storage_state="cookie_login") # cookie

    # Open new page
    page = context.new_page()
    
    # page.set_extra_http_headers({"myHeader" : "myValue"})
    
    # Go to https://www.tianyancha.com/organize/b5df63030
    page.goto("https://www.tianyancha.com/organize/b5df63030")

    # try:
    #     df = pd.read_excel("aa.xlsx")
    # except:
    #     df = pd.DataFrame(columns=['公司名称','公司全名','参与轮次','投资时间','投资金额','产品介绍','URL'])
    #     df.to_excel("aa.xlsx")

    for page_choose in range(1,60):
        
        try:
            page.locator("div:nth-child(7) > div > div:nth-child(2) > .table-footer > .pagination > .pagination-wrap > .pageWrap > div:nth-child(%s)"% page_choose).click()
    
            ff = page.query_selector("[data-dim=publicInvestment]")
            
            kk = ff.query_selector_all("xpath=//td")
            url = ff.query_selector_all("[class=link-click]")
            
            for oo in range(0,10):
                
                vc = tianyan_vc()
                
                for qq in range(8,14):
                    print(kk[oo*7+qq].inner_text())
                
                vc.company_name = kk[oo*7+8].inner_text()
                vc.company_full_name = kk[oo*7+9].inner_text()
                vc.company_vc_state = kk[oo*7+10].inner_text()
                vc.company_investment_time = kk[oo*7+11].inner_text()
                vc.company_investment_amount = kk[oo*7+12].inner_text()
                vc.company_describe = kk[oo*7+13].inner_text()
                
                # print("https://www.tianyancha.com"+url[oo*2-1].get_attribute("href"))
                
                vc.URL = "https://www.tianyancha.com"+url[oo*2-1].get_attribute("href")
                
                df = df.append({'公司名称':vc.company_name,'公司全名':vc.company_full_name,
                                '参与轮次':vc.company_vc_state,'投资时间':vc.company_investment_time,'投资金额':vc.company_investment_amount,
                                '产品介绍':vc.company_describe,'URL':vc.URL },ignore_index = True)
            # break
        except:
            pass

    df.to_excel("aa.xlsx")
    
    
    time.sleep(2000)


with sync_playwright() as playwright:
    run(playwright)
