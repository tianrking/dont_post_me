import requests
from bs4 import BeautifulSoup

cookies = {
    'TrackingId': '4589f2e0-696f-4393-b26a-5923304e3451',
    'optimizelyEndUserId': 'oeu1667965847787r0.5770187153075134',
    'ai_user': '31hdu|2022-11-09T03:50:48.124Z',
    '_vwo_uuid_v2': 'D5AB948A6ED181CB3ACFDFE8F8A705BBC|94a4b2c2e17b71d341ccc9f6114858a2',
    'AdvTrackingCookieId': '8415a68b-5d65-4637-ab04-2a63962ca044',
    '_vwo_uuid': 'D5AB948A6ED181CB3ACFDFE8F8A705BBC',
    '_vis_opt_exp_188_combi': '2',
    'LPVID': 'M1YzY5MWQ4NDBhNWE3YjNh',
    '_hjSessionUser_31101': 'eyJpZCI6ImNlOWVhM2I3LWQzZDYtNTY1OS1iMzdmLThhMGZjMTMxOWJiMSIsImNyZWF0ZWQiOjE2Njc5NjU4NDg2NzMsImV4aXN0aW5nIjp0cnVlfQ==',
    'CCPAAllowCookie': 'Allow',
    'TrackingId': 'd7bd8659-fa25-4f39-bf26-a5923304e345',
    '_gcl_au': '1.1.1421422662.1667987130',
    '_hjSessionUser_483537': 'eyJpZCI6IjYyYzY2MTNmLWFhMmItNWFlNC04NjM2LTg2M2Q0MzEyZTA2ZCIsImNyZWF0ZWQiOjE2Njc5ODcxNTA3NDcsImV4aXN0aW5nIjpmYWxzZX0=',
    '_fbp': 'fb.2.1667987150981.1057137883',
    '_clck': '12unjnx|1|f6f|0',
    'AdvTrackingDeviceId': '4ffe2248d4429793fab9ac48250cd747',
    'ARRAffinity': '2c2a5fcfbd91c0c1b848bdc7ab99ad1a54d9935a2d73bc9cb44a9ec5b9db4165',
    'ARRAffinitySameSite': '2c2a5fcfbd91c0c1b848bdc7ab99ad1a54d9935a2d73bc9cb44a9ec5b9db4165',
    '_gid': 'GA1.2.1916025213.1668406698',
    'ln_or': 'd',
    '_vis_opt_s': '4%7C',
    '_vis_opt_test_cookie': '1',
    '_hjIncludedInSessionSample': '0',
    '_hjSession_31101': 'eyJpZCI6ImM3Y2ZiMTlkLTVkNzktNDI5Yi1hNDRkLTNkYzcwN2FiYzhkMyIsImNyZWF0ZWQiOjE2Njg0OTExODU2NTUsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjIncludedInPageviewSample': '1',
    '_hjAbsoluteSessionInProgress': '1',
    '_vwo_ds': '3%3Aa_0%2Ct_0%3A0%241667965848%3A0.25431489%3A%3A10_0%3A3_0%2C2_0%2C1_0%3A1',
    'LPSID-30800048': 'W9u_Qi2zTMusT48CnJqhjg',
    'ASP.NET_SessionId': 'mbijavlokpk0lzgxhjaxzfop',
    'x-ms-routing-name': 'self',
    'TiPMix': '30.01525839572592',
    'tabSliceOut': '9999',
    '_vwo_sn': '525339%3A10',
    '_ga_CFPK80LF7Y': 'GS1.1.1668491185.8.1.1668491422.46.0.0',
    '_ga': 'GA1.2.89835254.1667965849',
}

headers = {
    'authority': 'www.advantech.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'TrackingId=4589f2e0-696f-4393-b26a-5923304e3451; optimizelyEndUserId=oeu1667965847787r0.5770187153075134; ai_user=31hdu|2022-11-09T03:50:48.124Z; _vwo_uuid_v2=D5AB948A6ED181CB3ACFDFE8F8A705BBC|94a4b2c2e17b71d341ccc9f6114858a2; AdvTrackingCookieId=8415a68b-5d65-4637-ab04-2a63962ca044; _vwo_uuid=D5AB948A6ED181CB3ACFDFE8F8A705BBC; _vis_opt_exp_188_combi=2; LPVID=M1YzY5MWQ4NDBhNWE3YjNh; _hjSessionUser_31101=eyJpZCI6ImNlOWVhM2I3LWQzZDYtNTY1OS1iMzdmLThhMGZjMTMxOWJiMSIsImNyZWF0ZWQiOjE2Njc5NjU4NDg2NzMsImV4aXN0aW5nIjp0cnVlfQ==; CCPAAllowCookie=Allow; TrackingId=d7bd8659-fa25-4f39-bf26-a5923304e345; _gcl_au=1.1.1421422662.1667987130; _hjSessionUser_483537=eyJpZCI6IjYyYzY2MTNmLWFhMmItNWFlNC04NjM2LTg2M2Q0MzEyZTA2ZCIsImNyZWF0ZWQiOjE2Njc5ODcxNTA3NDcsImV4aXN0aW5nIjpmYWxzZX0=; _fbp=fb.2.1667987150981.1057137883; _clck=12unjnx|1|f6f|0; AdvTrackingDeviceId=4ffe2248d4429793fab9ac48250cd747; ARRAffinity=2c2a5fcfbd91c0c1b848bdc7ab99ad1a54d9935a2d73bc9cb44a9ec5b9db4165; ARRAffinitySameSite=2c2a5fcfbd91c0c1b848bdc7ab99ad1a54d9935a2d73bc9cb44a9ec5b9db4165; _gid=GA1.2.1916025213.1668406698; ln_or=d; _vis_opt_s=4%7C; _vis_opt_test_cookie=1; _hjIncludedInSessionSample=0; _hjSession_31101=eyJpZCI6ImM3Y2ZiMTlkLTVkNzktNDI5Yi1hNDRkLTNkYzcwN2FiYzhkMyIsImNyZWF0ZWQiOjE2Njg0OTExODU2NTUsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=1; _vwo_ds=3%3Aa_0%2Ct_0%3A0%241667965848%3A0.25431489%3A%3A10_0%3A3_0%2C2_0%2C1_0%3A1; LPSID-30800048=W9u_Qi2zTMusT48CnJqhjg; ASP.NET_SessionId=mbijavlokpk0lzgxhjaxzfop; x-ms-routing-name=self; TiPMix=30.01525839572592; tabSliceOut=9999; _vwo_sn=525339%3A10; _ga_CFPK80LF7Y=GS1.1.1668491185.8.1.1668491422.46.0.0; _ga=GA1.2.89835254.1667965849',
    'if-modified-since': 'Tue, 15 Nov 2022 05:48:09 GMT',
    'referer': 'https://www.advantech.com/en/partners/channel',
    'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42',
}

response = requests.get('https://www.advantech.com/en/partners/channel/690',headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

Products_Direction = soup.find("div",attrs={'class':'content','id':'content2'}).find("h4").get_text()

products_list_temp = soup.find("div",attrs={'class':'content','id':'content2'}).find_all("li")
products_list = []
for i in products_list_temp :
    products_list.append(i.find("a").get_text())

print(products_list)
