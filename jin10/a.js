import axios from 'axios'

var config = {
   method: 'get',
   url: 'https://www.jin10.com/flash_newest.js?t=1645929628705',
   headers: { 
      'authority': 'www.jin10.com', 
      'sec-ch-ua': '^\\^', 
      'sec-ch-ua-mobile': '?0', 
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36', 
      'sec-ch-ua-platform': '^\\^Windows^\\^', 
      'accept': '*/*', 
      'sec-fetch-site': 'same-origin', 
      'sec-fetch-mode': 'no-cors', 
      'sec-fetch-dest': 'script', 
      'referer': 'https://www.jin10.com/', 
      'accept-language': 'zh-TW,zh-HK;q=0.9,zh;q=0.8,en;q=0.7,zh-CN;q=0.6,en-GB;q=0.5,en-US;q=0.4', 
      'cookie': 'Hm_lvt_522b01156bb16b471a7e2e6422d272ba=1645929399; sound=1; notify=2; jinSize=normal; kind_g=^%^5B^%^223^%^22^%^2C^%^227^%^22^%^5D; trend=1; x-token=; UM_distinctid=17f3909bf905e1-028195c3436eaa-a3e3164-144000-17f3909bf91a26; CNZZDATA1000171913=1230279298-1645928760-^%^7C1645928760; CNZZDATA1253039837=1625177336-1645922780-^%^7C1645922780; Hm_lpvt_522b01156bb16b471a7e2e6422d272ba=1645929551'
   }
};

axios(config)
.then(function (response) {
   console.log(JSON.stringify(response.data));
})
.catch(function (error) {
   console.log(error);
});