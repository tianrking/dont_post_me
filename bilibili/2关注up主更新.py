from h11 import Data
import requests
import json

headers = {
    'authority': 'api.vc.bilibili.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://t.bilibili.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://t.bilibili.com/',
    'accept-language': 'zh-TW,zh-HK;q=0.9,zh;q=0.8,en;q=0.7,zh-CN;q=0.6,en-GB;q=0.5,en-US;q=0.4',
    'cookie': 'l=v; blackside_state=1; _uuid=BB4955E2-B10C7-DE27-1ADC-8BABBCCD510CF92540infoc; buvid3=289FA252-E57F-40C3-A478-BE5FF140C3B2148802infoc; buvid_fp_plain=289FA252-E57F-40C3-A478-BE5FF140C3B2148802infoc; SESSDATA=52bf95d3%2C1653806858%2Cca858%2Ab1; bili_jct=a9d2640fe340378a33810c588f7b1860; DedeUserID=10065982; DedeUserID__ckMd5=cd1be546af2af657; sid=6m971zqi; video_page_version=v_old_home; rpdid=|(JJklYJuRl|0J\'uYJ)kllRY); fingerprint3=882b7c03f91efe813f15e01f6235063c; fingerprint=163d1b9818cd58bf2f49f56784b8ecdc; fingerprint_s=55063244d616c0f24ec819f712515549; i-wanna-go-back=-1; b_ut=5; buvid4=378C49F0-FCEC-9CAE-16F3-B9E02ECCFA3973530-022012609-hsOooHO6YQXlDx45RYHiEQ%3D%3D; buvid_fp=51806dcb0cb5d74b5f96c64fc6c0ce61; innersign=0; b_lsid=AEC5E6D2_17F3A70EF3D; CURRENT_BLACKGAP=0; CURRENT_FNVAL=80; _dfcaptcha=22234dc1ce7145ec53e7426a52d7c545; LIVE_BUVID=AUTO6916459531447425; PVID=4; bp_video_offset_10065982=631860680843067500; bp_t_offset_10065982=631860680843067472',
}

params = (
    ('uid', '10065982'),
    ('offset_dynamic_id', '631734331494105092'),
    ('type', '268435455'),
    ('from', 'weball'),
    ('platform', 'web'),
)

response = requests.get('https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_history', headers=headers, params=params)

response = json.loads(response.text)
g = response['data']['cards']
for i in g:
    # JSON_data = json.loads(i)
    print(i['desc'])
    # break
# print(len(g))

# print(len(response))