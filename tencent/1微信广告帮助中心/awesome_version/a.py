import requests
import json

url = 'https://ad.weixin.qq.com/openapi/acms_files/get?filename=data'
rec = requests.get(url)
# rec = json.loads(rec.text)
f = open('data_all.txt','w')
f.write(rec.text)
f.close()

# curl 'https://ad.weixin.qq.com/openapi/acms_files/get?filename=data' \
#   -H 'authority: ad.weixin.qq.com' \
#   -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"' \
#   -H 'accept: application/json, text/plain, */*' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36 Edg/98.0.1108.51' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'referer: https://ad.weixin.qq.com/guide/term/193' \
#   -H 'accept-language: zh-TW,zh-CN;q=0.9,zh;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,zh-HK;q=0.4' \
#   -H 'cookie: pgv_pvid=3686684000; pac_uid=0_3cbd911c9ce83; pgv_info=ssid=s2798911544; ts_uid=9628394784; pgv_pvi=4654092288; pgv_si=s6420471808; uin=o0508195902; skey=@sEUq3VJWl; RK=hA9xBYtEcN; ptcz=f4917937db9babf5c19203049471a3e4d45ea1fe7b770ef9ea93e47e33c0c0f5' \
#   --compressed