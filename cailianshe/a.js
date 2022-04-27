// import { express } from 'express';
import { json } from 'express';
import fetch from 'node-fetch';
import request from 'request';
// var fetch = require('node-fetch');

// var headers = {
//     'Connection': 'keep-alive',
//     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
//     'Accept': 'application/json, text/plain, */*',
//     'Content-Type': 'application/json;charset=utf-8',
//     'sec-ch-ua-mobile': '?0',
//     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
//     'sec-ch-ua-platform': '"Windows"',
//     'Sec-Fetch-Site': 'same-origin',
//     'Sec-Fetch-Mode': 'cors',
//     'Sec-Fetch-Dest': 'empty',
//     'Referer': 'https://www.cls.cn/telegraph',
//     'Accept-Language': 'zh-TW,zh-HK;q=0.9,zh;q=0.8,en;q=0.7,zh-CN;q=0.6,en-GB;q=0.5,en-US;q=0.4',
//     'If-None-Match': 'W/"28c2-X0O5ToV+Bo+BEkphYl8yKLoLPac"',
//     'Cookie': 'HWWAFSESID=3a3d276fad28eb8931; HWWAFSESTIME=1646659798349; hasTelegraphRemind=on; hasTelegraphSound=on; vipNotificationState=on; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1646659764,1646659766; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1646659766; hasTelegraphNotification=off'
// };

// var options = {
//     url: 'https://www.cls.cn/nodeapi/refreshTelegraphList?app=CailianpressWeb&lastTime=1646659780&os=web&sv=7.7.5&sign=639d4a54e68a1270edb70d96f13b9112',
//     headers: headers
// };

// function callback(error, response, body) {
//     if (!error && response.statusCode == 200) {
//         console.log(body);
//     }
// }

// request(options, callback);


fetch("https://www.jin10.com/flash_newest.js?t=1646661829038", {
  "headers": {
    "accept": "*/*",
    "accept-language": "zh-TW,zh-HK;q=0.9,zh;q=0.8,en;q=0.7,zh-CN;q=0.6,en-GB;q=0.5,en-US;q=0.4",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin"
  },
  "referrer": "https://www.jin10.com/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET",
  "mode": "cors",
  "credentials": "include"
}).then(res => res.json()); //then(res => res.json())
// .then(json => console.log(json));
console.log(res.json())