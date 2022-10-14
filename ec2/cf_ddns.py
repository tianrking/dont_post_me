import requests
import json

class A:
    email = 'xxx@gmail.com'
    key = 'xxx'
    zone = 'xxx'
    ddns_url = 'xxx'

_cf = A()

headers = {
    'X-Auth-Email': _cf.email,
    'X-Auth-Key': _cf.key,
    'Content-Type': 'application/json',
}

json_data = {
    'type': 'A',
    'name': 'abc',
    'content': '1.2.3.5',
    'ttl': 60,
    'proxied': False
}

url = 'https://api.cloudflare.com/client/v4/zones/%s/dns_records' % _cf.zone

def _delete_dns():
    response_all_domain = requests.get(url, headers=headers)
    response_all_domain =  json.loads(response_all_domain.text)['result']
    # print(len(response_all_domain))
    for domain in response_all_domain:
        if domain['name'] == _cf.ddns_url:
            del_url = url + "/" +domain['id']
            res = requests.delete(del_url, headers=headers)
            print("delete " + res.text )
        
    
# print(response_all_domain)

for i in range(1,100):
    _delete_dns()
    json_data['content'] = "1.2.3.%s" % str(i)
    json_data['name'] = _cf.ddns_url
    print(json_data)
    response = requests.post(url, headers=headers, json=json_data)
    print(response.text)