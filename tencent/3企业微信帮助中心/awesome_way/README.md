##  怎样获取到接口

- burpsuite
- wireshark
- chrome f12

```bash
# curl 'https://open.work.weixin.qq.com/help2/getQusList?lang=zh_CN&ajax=1&f=json&random=310321' \
#   -H 'authority: open.work.weixin.qq.com' \
#   -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"' \
#   -H 'accept: application/json, text/plain, */*' \
#   -H 'content-type: application/json' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36 Edg/98.0.1108.51' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'origin: https://open.work.weixin.qq.com' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'referer: https://open.work.weixin.qq.com/help2/pc/15405?person_id=1' \
#   -H 'accept-language: zh-TW,zh-CN;q=0.9,zh;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,zh-HK;q=0.4' \
#   -H 'cookie: pgv_pvid=3686684000; pac_uid=0_3cbd911c9ce83; pgv_info=ssid=s2798911544; pgv_pvi=4654092288; pgv_si=s6420471808; wwrtx.ref=direct; wwrtx.c_gdpr=0; wwrtx.refid=413075501944711; __utma=114362329.896737070.1644833346.1644833346.1644833346.1; __utmc=114362329; __utmz=114362329.1644833346.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_f2ba645ba13636ba52b0234381f51cbc=1644833347; Hm_lpvt_f2ba645ba13636ba52b0234381f51cbc=1644833970; uin=o0508195902; skey=@sEUq3VJWl; RK=hA9xBYtEcN; ptcz=f4917937db9babf5c19203049471a3e4d45ea1fe7b770ef9ea93e47e33c0c0f5; wwrtx.i18n_lan=cht' \
#   --data-raw '{"person_id":1,"doc_id":15405}' \
#   --compressed
```

## 思路 

配置好代理池 直接暴力遍历即可  得到数据再用pandas清洗
