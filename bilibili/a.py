import requests
import json

headers = {
    'authority': 'api.bilibili.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
    'sec-ch-ua-platform': '"macOS"',
    'accept': '*/*',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'script',
    'referer': 'https://www.bilibili.com/video/BV1ca4y1n7u3?from=search&seid=3958852060761366853&spm_id_from=333.337.0.0',
    'accept-language': 'zh-TW,zh-CN;q=0.9,zh;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,zh-HK;q=0.4',
    '$cookie': 'buvid3=A5B9B474-4454-E46A-5D70-1C0FCFD3111D15289infoc; _uuid=110E7B10DA-931E-C610E-1448-5BD10456C1041326211infoc; buvid4=44EEDBFC-7552-AA0F-D20A-78B97184942128868-022021713-WK3KqOndA/qKg1WB0wdgrg%3D%3D; blackside_state=1; rpdid=|()Y|m)l)mJ0J\'uYRl|~YYkk; i-wanna-go-back=-1; fingerprint=69ac64701246e230a3220ddb51519c5a; buvid_fp_plain=undefined; buvid_fp=dcf94c4581a7fe29771814772f1f9b87; SESSDATA=1fb57422%2C1660649390%2Cfd34c%2A21; bili_jct=ee025a7fc5ca184958af7e9d18fd6cbe; DedeUserID=10065982; DedeUserID__ckMd5=cd1be546af2af657; sid=c32mg3bm; b_ut=5; b_lsid=E21EA8FE_17F1516C148; bp_video_offset_10065982=629159459865830000; CURRENT_BLACKGAP=0; LIVE_BUVID=AUTO5716453263384305; innersign=1; CURRENT_FNVAL=4048; PVID=1',
}

params = (
    ('callback', 'jQuery33109325720014143493_1645326695287'),
    ('jsonp', 'jsonp'),
    ('next', '0'),
    ('type', '1'),
    ('oid', '670842482'),
    ('mode', '3'),
    ('plat', '1'),
    ('_', '1645326695288'),
)

response = requests.get('https://api.bilibili.com/x/v2/reply/main', headers=headers, params=params)
# response = json.loads(response)
# print(response.text)

print(len(g))