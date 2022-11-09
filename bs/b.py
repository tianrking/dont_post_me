import requests

headers = {
    'authority': 'www.advantech.com',
    'accept': '*/*',
    'accept-language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'optimizelyEndUserId=oeu1667965847787r0.5770187153075134; ASLBSA=000342bdebd053a07f29c058ac6fef53abba20a8260e9de3bdc6fe4e7cc8aaea5789; ASLBSACORS=000342bdebd053a07f29c058ac6fef53abba20a8260e9de3bdc6fe4e7cc8aaea5789; ai_user=31hdu|2022-11-09T03:50:48.124Z; _vwo_uuid_v2=D5AB948A6ED181CB3ACFDFE8F8A705BBC|94a4b2c2e17b71d341ccc9f6114858a2; AdvTrackingCookieId=8415a68b-5d65-4637-ab04-2a63962ca044; AdvTrackingDeviceId=821503bad72ddfdc01bc4ba57fc399b3; ln_or=d; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D5AB948A6ED181CB3ACFDFE8F8A705BBC; _vis_opt_exp_188_combi=2; ASP.NET_SessionId=rnr4qb1vrm1avhdccsppmdqr; ARRAffinity=c27b3ad56fe80b02e48983c44fe42b5114795379a4cf3e78115a491667d8d352; ARRAffinitySameSite=c27b3ad56fe80b02e48983c44fe42b5114795379a4cf3e78115a491667d8d352; _gid=GA1.2.1115640071.1667965853; LPVID=M1YzY5MWQ4NDBhNWE3YjNh; _hjSessionUser_31101=eyJpZCI6ImNlOWVhM2I3LWQzZDYtNTY1OS1iMzdmLThhMGZjMTMxOWJiMSIsImNyZWF0ZWQiOjE2Njc5NjU4NDg2NzMsImV4aXN0aW5nIjp0cnVlfQ==; CCPAAllowCookie=Allow; _vwo_ds=3%3Aa_0%2Ct_0%3A0%241667965848%3A0.25431489%3A%3A10_0%3A2_0%2C1_0%3A1; x-ms-routing-name=self; _hjSession_31101=eyJpZCI6ImY3OTQyZTUxLTFmMWEtNDcyMC1iYzE3LTgwMTAzOTVhNzBkYiIsImNyZWF0ZWQiOjE2Njc5NzYyMzc0NTUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; TiPMix=76.09200154825581; LPSID-30800048=4QlJugNwSAKVFcoSYJZ3pQ; tabSliceOut=9999; _vwo_sn=8929%3A5; _ga=GA1.2.89835254.1667965849; _ga_CFPK80LF7Y=GS1.1.1667975249.3.1.1667977331.11.0.0; ai_session=O+/QZ|1667977450764.4|1667979549199.1',
    'origin': 'https://www.advantech.com',
    'referer': 'https://www.advantech.com/en/partners/channel',
    'request-context': 'appId=cid-v1:0301b09e-c5f2-4bbf-8e16-cc27870a6d7f',
    'request-id': '|r1rZH.8rB5K',
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
    'Countrys[0][key]': 'Brazil',
    'Countrys[0][value][]': '',
    'KeyWord': '',
}

response = requests.post('https://www.advantech.com/en/Partners/ChannelSearch', cookies=cookies, headers=headers, data=data)