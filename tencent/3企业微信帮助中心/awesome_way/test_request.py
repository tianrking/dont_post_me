import requests
import json

headers = {
    'authority': 'open.work.weixin.qq.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://open.work.weixin.qq.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://open.work.weixin.qq.com/help2/pc/16526',
    'accept-language': 'zh-TW,zh-CN;q=0.9,zh;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,zh-HK;q=0.4',
    'cookie': 'pgv_pvid=3686684000; pac_uid=0_3cbd911c9ce83; pgv_pvi=4654092288; wwrtx.c_gdpr=0; __utma=114362329.896737070.1644833346.1644833346.1644833346.1; __utmz=114362329.1644833346.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_f2ba645ba13636ba52b0234381f51cbc=1644833347; RK=hA9xBYtEcN; ptcz=f4917937db9babf5c19203049471a3e4d45ea1fe7b770ef9ea93e47e33c0c0f5; wwrtx.i18n_lan=cht; pgv_info=ssid=s2791877920; pgv_si=s383571968; wwrtx.ref=direct; wwrtx.refid=6308703232183814',
}

params = (
    ('lang', 'zh_CN'),
    ('ajax', '1'),
    ('f', 'json'),
    ('random', '630161'),
)

## doc id 编号为主文档对应序号
# data = '{"person_id":1,"doc_id":15405}'
data = '{"person_id":1,"doc_id":16652}'

res = requests.post('https://open.work.weixin.qq.com/help2/getQusList', headers=headers, params=params, data=data)
res = json.loads(res.text)

Q = res['data']['helpdocument']['qusList'][0]['title']
A_md = res['data']['helpdocument']['qusList'][0]['content_md']
A_URL = "https://open.work.weixin.qq.com/help2/pc/16652/"+str(res['data']['helpdocument']['id'])
print(Q,A_URL)