import requests
import pandas as pd
from bs4 import BeautifulSoup

cookies = {
    'optimizelyEndUserId': 'oeu1667965847787r0.5770187153075134',
    'ASLBSA': '000342bdebd053a07f29c058ac6fef53abba20a8260e9de3bdc6fe4e7cc8aaea5789',
    'ASLBSACORS': '000342bdebd053a07f29c058ac6fef53abba20a8260e9de3bdc6fe4e7cc8aaea5789',
    'ai_user': '31hdu|2022-11-09T03:50:48.124Z',
    '_vwo_uuid_v2': 'D5AB948A6ED181CB3ACFDFE8F8A705BBC|94a4b2c2e17b71d341ccc9f6114858a2',
    'AdvTrackingCookieId': '8415a68b-5d65-4637-ab04-2a63962ca044',
    'AdvTrackingDeviceId': '821503bad72ddfdc01bc4ba57fc399b3',
    'ln_or': 'd',
    '_vis_opt_s': '1%7C',
    '_vis_opt_test_cookie': '1',
    '_vwo_uuid': 'D5AB948A6ED181CB3ACFDFE8F8A705BBC',
    '_vis_opt_exp_188_combi': '2',
    'ASP.NET_SessionId': 'rnr4qb1vrm1avhdccsppmdqr',
    'ARRAffinity': 'c27b3ad56fe80b02e48983c44fe42b5114795379a4cf3e78115a491667d8d352',
    'ARRAffinitySameSite': 'c27b3ad56fe80b02e48983c44fe42b5114795379a4cf3e78115a491667d8d352',
    '_gid': 'GA1.2.1115640071.1667965853',
    'LPVID': 'M1YzY5MWQ4NDBhNWE3YjNh',
    'LPSID-30800048': 'ZKsaAqsVTLqxWBv69kWuIg',
    '_hjSessionUser_31101': 'eyJpZCI6ImNlOWVhM2I3LWQzZDYtNTY1OS1iMzdmLThhMGZjMTMxOWJiMSIsImNyZWF0ZWQiOjE2Njc5NjU4NDg2NzMsImV4aXN0aW5nIjp0cnVlfQ==',
    'CCPAAllowCookie': 'Allow',
    'tabSliceOut': '9999',
    '_ga': 'GA1.2.89835254.1667965849',
    '_vwo_sn': '4863',
    '_vwo_ds': '3%3Aa_0%2Ct_0%3A0%241667965848%3A0.25431489%3A%3A10_0%3A2_0%2C1_0%3A1',
    'x-ms-routing-name': 'self',
    'TiPMix': '24.61958793907003',
    '_ga_CFPK80LF7Y': 'GS1.1.1667971007.2.1.1667972685.60.0.0',
    'ai_session': 'AvNt0|1667973154639|1667973154639',
}

headers = {
    'authority': 'www.advantech.com',
    'accept': '*/*',
    'accept-language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'optimizelyEndUserId=oeu1667965847787r0.5770187153075134; ASLBSA=000342bdebd053a07f29c058ac6fef53abba20a8260e9de3bdc6fe4e7cc8aaea5789; ASLBSACORS=000342bdebd053a07f29c058ac6fef53abba20a8260e9de3bdc6fe4e7cc8aaea5789; ai_user=31hdu|2022-11-09T03:50:48.124Z; _vwo_uuid_v2=D5AB948A6ED181CB3ACFDFE8F8A705BBC|94a4b2c2e17b71d341ccc9f6114858a2; AdvTrackingCookieId=8415a68b-5d65-4637-ab04-2a63962ca044; AdvTrackingDeviceId=821503bad72ddfdc01bc4ba57fc399b3; ln_or=d; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D5AB948A6ED181CB3ACFDFE8F8A705BBC; _vis_opt_exp_188_combi=2; ASP.NET_SessionId=rnr4qb1vrm1avhdccsppmdqr; ARRAffinity=c27b3ad56fe80b02e48983c44fe42b5114795379a4cf3e78115a491667d8d352; ARRAffinitySameSite=c27b3ad56fe80b02e48983c44fe42b5114795379a4cf3e78115a491667d8d352; _gid=GA1.2.1115640071.1667965853; LPVID=M1YzY5MWQ4NDBhNWE3YjNh; LPSID-30800048=ZKsaAqsVTLqxWBv69kWuIg; _hjSessionUser_31101=eyJpZCI6ImNlOWVhM2I3LWQzZDYtNTY1OS1iMzdmLThhMGZjMTMxOWJiMSIsImNyZWF0ZWQiOjE2Njc5NjU4NDg2NzMsImV4aXN0aW5nIjp0cnVlfQ==; CCPAAllowCookie=Allow; tabSliceOut=9999; _ga=GA1.2.89835254.1667965849; _vwo_sn=4863; _vwo_ds=3%3Aa_0%2Ct_0%3A0%241667965848%3A0.25431489%3A%3A10_0%3A2_0%2C1_0%3A1; x-ms-routing-name=self; TiPMix=24.61958793907003; _ga_CFPK80LF7Y=GS1.1.1667971007.2.1.1667972685.60.0.0; ai_session=AvNt0|1667973154639|1667973154639',
    'origin': 'https://www.advantech.com',
    'referer': 'https://www.advantech.com/en/partners/channel',
    # 'request-context': 'appId=cid-v1:0301b09e-c5f2-4bbf-8e16-cc27870a6d7f',
    'request-id': '|r1rZH.LI2VS',
    'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'Countrys[0][key]': 'Uzbekistan',
    'Countrys[0][value][]': '',
    # 'Countrys[1][key]': 'Cyprus',
    # 'Countrys[1][value][]': '',
    'KeyWord': '',
}

response = requests.post('https://www.advantech.com/en/Partners/ChannelSearch', cookies="", headers=headers, data=data)

    
soup = BeautifulSoup(response.text, "html.parser")
    
# print(soup.prettify())  

# titles = soup.find_all("p", class_="summary", limit=3)
# parents = result.find_parents("h3")
# title.select_one("a")
# title.select_one("a").get("href")
# title.select_one("a").getText()

class _crawl_data:
    
    Name = ""
    Tel = ""
    Url = ""
    Email = ""
    Country = ""
    Location = ""
    Industry_Area = ""
    Description = ""
    Logo = ""
    More = ""
    Products_Direction = ""
    
    def print_value(self):
        print(self.Name)
        print(self.Tel)
        print(self.Url)
        print(self.Email)
        print(self.Country)
        print(self.Description)
        print(self.More)
        print(self.Industry_Area)
        print(self.Logo)
        print(self.Location)
        print(self.Products_Direction)

result = soup.find_all("li",class_="partner-list")


df = pd.DataFrame(columns=["Name", "Tel","Email","Description","Industry_Area","Url","Country","Logo"])

with open("a.html", 'w',encoding="utf-8") as fp:
    # write the current soup content
    fp.write(soup.prettify())

num_flag = 1

for i in result:
    
    
    # df.iloc['']
    
    ii = i.find_all("a")
    Crawl_Data = _crawl_data()
    products_list = []
    
    try: 
        # Crawl_Data.Url = ii[1].get("href")
        Crawl_Data.Url = i.find("div","partner-info").find("a").get("href")
        
        
        # Crawl_Data.Name = ii[1].getText() 
        Crawl_Data.Name = i.find("div",class_ = "parter-name").getText() 
        
        # Crawl_Data.Tel = ii[2].getText()
        Crawl_Data.Email = i.find("div",class_ = "mail").find("a").getText()
        # Crawl_Data.Email = ii[3].getText()
        Crawl_Data.Tel = i.find("div",class_ = "phone").find("a").getText()
        
        Crawl_Data.Description = i.find("div",class_ = "description").find("p").getText()
        Crawl_Data.More = "https://www.advantech.com.cn" + i.find("div",class_="btnwrap").find("a").get("href")
        Crawl_Data.Logo = i.find("div",class_ = "logo")["style"].split("background-image: url(")[1][:-2]
        
        try: 
            Crawl_Data.Country = i.find("div",class_ = "country").getText()
        except:
            Crawl_Data.Country = ""
            print("Country not avaliabale")
        
        try:    
            Crawl_Data.Industry_Area = i.find("div",class_ = "industry-area").find("li").getText()
        except:
            Crawl_Data.Industry_Area = ""
            print("Dont have tage")

        response_temp = requests.get(Crawl_Data.More, headers=headers)
        soup_temp = BeautifulSoup(response_temp.text, "html.parser")
        Crawl_Data.Products = soup_temp.find("div",class_="advan-content")
        Crawl_Data.Products_Direction = soup_temp.find("div",attrs={'class':'content','id':'content2'}).find("h4").get_text()
        products_list_temp = soup_temp.find("div",attrs={'class':'content','id':'content2'}).find_all("li")
        
        for i in products_list_temp :
            products_list.append(i.find("a").get_text())
                
        print(num_flag,"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
        
    
    except:
        # print(ii)
        print(num_flag,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        pass
    #  Crawl_Data.Tel,Crawl_Data.Email,Crawl_Data.Description,Crawl_Data.Industry_Area,Crawl_Data.Url,Crawl_Data.Country,Crawl_Data.Logo   
    df = df.append({"Name":Crawl_Data.Name, 
                    "Tel":Crawl_Data.Tel,
                    "Email":Crawl_Data.Email,
                    "Description":Crawl_Data.Description,
                    "Industry_Area":Crawl_Data.Industry_Area,
                    "Url":Crawl_Data.Url,
                    "Country":Crawl_Data.Country,
                    "Products_Direction":Crawl_Data.Products_Direction,
                    "Products_List": products_list,
                    "More":Crawl_Data.More,
                    "Logo":Crawl_Data.Logo
                    }, ignore_index = True)
    
    # Crawl_Data.Products = Crawl_Data.Products.find("div",class_ = "content-wrap")
    # Crawl_Data.Products = Crawl_Data.Products.find("h4").getText()

    # Crawl_Data.print_value()
    
    num_flag = num_flag + 1 
    
    # if num_flag == 5:
    #     break

df.to_excel("a.xlsx", index=False, header=True)
