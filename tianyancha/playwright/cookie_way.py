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
    

def run(playwright: Playwright) -> None:
    
    # Python
    proxy_to_use = {
        'server': '123.123.123.123:80'
    }

    browser = playwright.chromium.launch(headless=True) # proxy=proxy_to_use,
    context = browser.new_context(storage_state="cookie_login")

    # Open new page
    page = context.new_page()

    # Go to https://www.tianyancha.com/
    # page.goto("https://www.tianyancha.com/")

    # Go to https://www.tianyancha.com/organize/b5df63030
    page.goto("https://www.tianyancha.com/organize/b5df63030")

    # ---------------------
    # context.close()
    # browser.close()
    

    ### company name
    
    # First company
    # "div:nth-child(7) > div > div:nth-child(2) > .table-wrap > tbody > tr > td:nth-child(2) > .img-toco-wrap > div:nth-child(2) > .right-info" 
    # 2nd - 10th company
    # "div:nth-child(7) > div > div:nth-child(2) > .table-wrap > tbody > tr:nth-child(2) > td:nth-child(2) > .img-toco-wrap > div:nth-child(2) > .right-info"
    # "div:nth-child(7) > div > div:nth-child(2) > .table-wrap > tbody > tr:nth-child(3) > td:nth-child(2) > .img-toco-wrap > div:nth-child(2) > .right-info"
    # "div:nth-child(7) > div > div:nth-child(2) > .table-wrap > tbody > tr:nth-child(10) > td:nth-child(2) > .img-toco-wrap > div:nth-child(2) > .right-info"
    
    # handle = page.query_selector("div:nth-child(7) > div > div:nth-child(2) > .table-wrap > tbody > tr:nth-child(2) > td:nth-child(2) > .img-toco-wrap > div:nth-child(2) > .right-info")
    # print(handle.text_content())
    # "div:nth-child(7) > div > div:nth-child(2) > .table-wrap > tbody > tr:nth-child(2) > td:nth-child(4)"
    # "div:nth-child(7) > div > div:nth-child(2) > .table-wrap > tbody > tr:nth-child(3) > td:nth-child(4)"

    
    ## PAGE CHANGE
    #
    #     # Click div:nth-child(7) > div > div:nth-child(2) > .table-footer > .pagination > .pagination-wrap > .pageWrap > div:nth-child(2)
    #    page.locator("div:nth-child(7) > div > div:nth-child(2) > .table-footer > .pagination > .pagination-wrap > .pageWrap > div:nth-child(2)").click()
    #     # Click div:nth-child(7) > div > div:nth-child(2) > .table-footer > .pagination > .pagination-wrap > .pageWrap > div:nth-child(4)
    #    page.locator("div:nth-child(7) > div > div:nth-child(2) > .table-footer > .pagination > .pagination-wrap > .pageWrap > div:nth-child(4)").click()

    for page_choose in range(1,40):
        
        # page_choose = 
        page.locator("div:nth-child(7) > div > div:nth-child(2) > .table-footer > .pagination > .pagination-wrap > .pageWrap > div:nth-child(%s)"% page_choose).click()
        # print(page_choose)
        # "div:nth-child(7) > div > div:nth-child(2) > .table-footer > .pagination > .pagination-wrap > .pageWrap > div:nth-child(5)"
        
        # try:
        #     for i in range (1,11):
        #         crawl_data = tianyan_vc()
        #         crawl_data.company_name = "div:nth-child(7) > div > div:nth-child(2) > .table-wrap > tbody > tr:nth-child(%s) > td:nth-child(2) > .img-toco-wrap > div:nth-child(2) > .right-info" % i
        #         crawl_data.company_name = page.query_selector(crawl_data.company_name)
        #         crawl_data.company_name = crawl_data.company_name.text_content()
                
        #         # crawl_data.company_full_name = "div:nth-child(7) > div > div:nth-child(2) > .table-wrap > tbody > tr:nth-child(%s) > td:nth-child(2) > .img-toco-wrap > div:nth-child(2) > .right-info" % i
        #         # crawl_data.company_full_name = page.query_selector(crawl_data.company_full_name)
        #         # crawl_data.company_full_name = crawl_data.company_full_name.text_content()
                
        #         # crawl_data.company_vc_agency = "div:nth-child(7) > div > div:nth-child(2) > .table-wrap > tbody > tr:nth-child(%s) > td:nth-child(2) > .img-toco-wrap > div:nth-child(2) > .right-info" % i
        #         # crawl_data.company_vc_agency = page.query_selector(crawl_data.company_vc_agency)
        #         # crawl_data.company_vc_agency = crawl_data.company_vc_agency.text_content()
        #         crawl_data.company_vc_agency = "创新工场"
                
        #         crawl_data.company_vc_state = "div:nth-child(7) > div > div:nth-child(2) > .table-wrap > tbody > tr:nth-child(%s) > td:nth-child(4)" % i 
        #         crawl_data.company_vc_state = page.query_selector(crawl_data.company_vc_state)
        #         crawl_data.company_vc_state = crawl_data.company_vc_state.text_content()
                
        #         # crawl_data.company_investment_amount = "div:nth-child(7) > div > div:nth-child(2) > .table-wrap > tbody > tr:nth-child(%s) > td:nth-child(2) > .img-toco-wrap > div:nth-child(2) > .right-info" % i
        #         # crawl_data.company_investment_amount = page.query_selector(crawl_data.company_investment_amount)
        #         # crawl_data.company_investment_amount = crawl_data.company_investment_amount.text_content()
                
        #         # crawl_data.company_investment_time = "div:nth-child(7) > div > div:nth-child(2) > .table-wrap > tbody > tr:nth-child(%s) > td:nth-child(2) > .img-toco-wrap > div:nth-child(2) > .right-info" % i
        #         # crawl_data.company_investment_time = page.query_selector(crawl_data.company_investment_time)
        #         # crawl_data.company_investment_time = crawl_data.company_investment_time.text_content()
                
        #         # all_quotes = page.query_selector_all('.quote')
        #         # for quote in all_quotes:
        #         #     text = quote.query_selector('.text').inner_text()
        #         #     author = quote.query_selector('.author').inner_text()
        #         #     print({'Author': author, 'Quote': text})
                
        #         print(crawl_data.company_vc_agency,crawl_data.company_name,crawl_data.company_vc_state,)
            
        #         # print(i)
        # except:
        #     pass

        
        # page.query_selector_all("xpath=//tbody")
        
        ff = page.query_selector("[data-dim=publicInvestment]")
        
        kk = ff.query_selector_all("xpath=//td")
        url = ff.query_selector_all("[class=link-click]")
        
        for oo in range(0,10):
            for qq in range(8,14):
                print(kk[oo*7+qq].inner_text())
            print(url[oo*2-1].get_attribute("href"))
            
        break 
    
    # Click div:nth-child(7) > div > div:nth-child(2) > .table-wrap > tbody > tr:nth-child(3) > td:nth-child(2) > .img-toco-wrap > div:nth-child(2) > .right-info
    # page.locator("div:nth-child(7) > div > div:nth-child(2) > .table-wrap > tbody > tr:nth-child(3) > td:nth-child(2) > .img-toco-wrap > div:nth-child(2) > .right-info").click()

    time.sleep(2000)


with sync_playwright() as playwright:
    run(playwright)
