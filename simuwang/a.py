import requests
import pandas as pd
import json

cookies = {
    'sajssdk_2015_cross_new_user': '1',
    'Hm_lvt_c3f6328a1a952e922e996c667234cdae': '1648023754',
    'qualified_investor': '0',
    'focus-certification-pop': '1',
    'need_update_password': '1',
    'smppw_tz_auth': '1',
    'certification': '1',
    'evaluation_result': '4',
    'sensorsdata2015jssdkcross': "%7B%22distinct_id%22%3A%2217fb65d759536b-00334f14191865-5617185b-1327104-17fb65d75961249%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217fb5ded2331db-074ccf990dfe15-5617185b-1327104-17fb5ded234123b%22%7D",
    'Hm_lpvt_c3f6328a1a952e922e996c667234cdae': '1648032054',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://dc.simuwang.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://dc.simuwang.com/',
    'Accept-Language': 'zh-TW,zh-HK;q=0.9,zh;q=0.8,en;q=0.7,zh-CN;q=0.6,en-GB;q=0.5,en-US;q=0.4',
    # Requests sorts cookies= alphabetically
    'Cookie': 'sajssdk_2015_cross_new_user=1; Hm_lvt_c3f6328a1a952e922e996c667234cdae=1648023754; qualified_investor=0; focus-certification-pop=1; need_update_password=1; smppw_tz_auth=1; certification=1; evaluation_result=4; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217fb65d759536b-00334f14191865-5617185b-1327104-17fb65d75961249%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217fb5ded2331db-074ccf990dfe15-5617185b-1327104-17fb5ded234123b%22%7D; Hm_lpvt_c3f6328a1a952e922e996c667234cdae=1648032054',
}

data = {
    'page': '3',
    'sort_name': 'ret',
    'sort_asc': 'desc',
    'condition': 'ret:4;',
    'USER_ID': '1830378',
}

response = requests.post('https://ppwapi.simuwang.com/ranking/company', headers=headers,  data=data)
response = json.loads(response.text)
print(response)

# session = requests.session()

# login_headers = {
#     'Connection': 'keep-alive',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
#     'Accept': 'application/json, text/plain, */*',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'sec-ch-ua-mobile': '?0',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
#     'sec-ch-ua-platform': '"Windows"',
#     'Origin': 'https://dc.simuwang.com',
#     'Sec-Fetch-Site': 'same-site',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Dest': 'empty',
#     'Referer': 'https://dc.simuwang.com/',
#     'Accept-Language': 'zh-TW,zh;q=0.9',
# }

# login_data = {
#   'username': '15773211225',
#   'password': 'Lyp82nlf',
#   'do_qualified': '1',
#   'reme': '1',
#   'NVCVal':"%7B%22a%22%3A%22FFFF0N00000000008289%22%2C%22c%22%3A%22FFFF0N00000000008289%3Anvc_register%3A1648046488417%3A0.3809806774833502%22%2C%22d%22%3A%22nvc_register%22%2C%22j%22%3A%7B%22test%22%3A1%7D%2C%22h%22%3A%7B%7D%2C%22b%22%3A%22221!uMCu%2Btu%2FqMA0n7xcSuBxC0JQ8GWB2wkmmUqAzyqVrvR3APJekCTURLz42HWBwYKQv1%2B7ZhB%2FHDO%2BOokvmuqvlb4SW6FE4yt1biEI5KQ%2FLgpf5abwrKqbFdGzfc676O2F0Xxrd4buz5hHp%2Bh62Zk%2FTciJBN0UR2Y0gXUyQmbPxmm4W0TqTsPwWNo6ZrcxRWH%2FK2Ec9SZ%2FP%2F9pAq68z090qL9Ezcd8Xab4vDBaYQZOz0LRKvoUNKLxCj%2FvwngXM%2FrC4X%2F0ht6%2BfsBklUv%2Br%2F0JywbU3Uj%2F4%2BJaOU5VCY0UN24JRnMLtNCjsNI1BHBnaDpXoH%2ByMI%2BKBPVXW0bnMU5ZJaaXuj%2FHsq6UgwY95PY5Aab2O0EDL5hpn65YxrqqML494QiWnwj7B2mi%2BFPxxxGheHFLCaym8g78GfckvV8i6Ml9vHHrLctINhhxl%2Fw1KuUowcJO%2Fen0ofyZ5%2BbmUPeZU8HbQxnAS2Z9qV2Q4PQ7NSPe%2BYHL8iExWKrUg%2BQ%2F11EQvOkBxBCPw2IGkRRQKbt0LmNHf9IxitLX%2BsEKiYtSAA7HilWZNut6jeivdR%2BUCAlc55uFOPgOmZGJhBBtjLNBWBoBzAY7fvVz7tdP8l9RGU5qvNaRLy%2FQN6iSlyHNCv6jLQTZpxa2PW%2FkrGbj%2Fp%2BcLm0lLGA82qx1omtmGFZ4%2FNzgahxtvULWcAFmC2T1qWssg%2FIKFFAS%2B9hVoqWVYNk4xVeTsUN3GomBCuIMwdEfu4GfHqYR2Z2vy%2BqZnROkGsnO8Xc4VdMlbcOMzFow1rFp1QXH%2F0pKY8q2mHaisdzaUGrMB1kVOmxnrv1qS204%2F3iVtJU92lEhvY6tIPUVMaFbjaPNatR0Xec0lOH4ukqmyq61yNg3Qf592kzXiYvJpOEdYWPQ01y9ARefg7%2FC%2BzfrYlZKodWhockINfDqvROD44viH7xdniko%2BcZBJaNxI03mjl1J0Ws17TqYWaBI19awOZjlSg%2BP1ffi38H0IA10caOtXZnAOSsbZ7kqIowcfiBGHp6vL7z6tKhGmu4sC2vPAlz29xik77xIOKk56bOY8N4x%2BmFYhVpCB0kEZ7%2FnbM3A0%2Bwp5W5s3NNddpbomiHd%2F2y6gkAJXJRgiitgCDLyKNTCjl8JlP6ydX9z244toF7j47yDn72g8J7GPYSuedbKLao5f1%2FELJdiaTvUGxesbHGzhFHBHg8L0ZMhxnMloRfNieGvaUHHAns2X6yf00wTOnoV22UbydohPPtjs7Py379Z%2BZbTxf9oTuLi1Zc2aTAjFKexVO5MXtOSFnxasvrNjmTX5UDtEpMhPV1t3TsogWPbCsPLl92MMdId8WukGcnelWiwcA8qAnQBacM4Ni8nDJ8JP7LftVdQSxWBNAoAcB30vyr3118ELztGBIaDJO87VHhKJ7gUL665RvgLLz54JuSdoZrW%2FNBdLrQxi21rK0%2BltBwMcokDtGcoErklDSl3QzgW2BGfx%2Bo%2Bi4jxHiga3xSlNf4XvRbX0EnjMVuKEVyts1FpUzN0vSp6QMDCSDwz8XAqLbnUoe82vvnAHYbdR%2BKzNvXw1z4Uk3yxd%2BWjF22szcTqsQVopZaGMpjFt5e2zAhgRqDrf0DERAB5XWcQe%2Bk%2BfAlqt6e7AYtoxRCzvGTtdLO3A6K5pKv%2Ff1PxnPBdHkCGvGK1slqDgGPwPuu172nhKivv%2B8IusFJAREWVbXrKGQhRdSWfF0SK%2Fg2adpSuDgPMB596BE5Y9xwqmHxYp46cvlJjn60YFGgeVhg6a4wsGHRYvHzjNJ%2BAiw2JXSnoPQuYt4ZyuhUEp9Rl%2FEkS6sFpc8DjECV005V1Qwo6BylUdJt74zfscHrQyBF4bo2ZgBfhy5cjiRlwXQMHrRbQrlHjdfFvnl2yfKFSGeOTg7lMPanJzTmJGc9iysVQrR0AVCtIjPj1Ojxz2XbfMLN2lQqG6LJasv2T6mPvnCFMoxzqDCr%2FeutvwBAPhBR5c2BDZSV4VoCjGnVaNkw8cwmo9CVRoOjJkycE%2FkGAjfNXZ8YdjtUUan3KmC622dXfSGZSZMa8K5QpKXxG7oPNd6TTyKwkApTwVGUJ4keXuoHqZN%2F1KD7mhn00uQiZYopOuejYztuTzBqEtGwCJHQV7xJjIQZKhVP6m4r2GErDLONjyCi%2FoqTwHirL4M1fGaquPumx3OImWdASiR1CKIXAIe3yVALVly5G7kuh8pBfilUG3YczezuNfvWM22e4d1aIKGXkchtZ2SzTmx6MbvEkk1CrGFe4g%2BRX1V6bTjcBf08tkUvX347ApK3RTiu6ojrUk7fU%2FiyfrK%2BT3EkOpF5u9HWWTLDUfe71uLDeOQv7xglvqdui8WlPjI0uIcIm5dW4t2ixUsnDBNm%2BlgPMmvY%2F6zGGG0T8U%2BzeDW%2Bm3yZXRvkj9zwY7UT6ztUUhdAlAkwbUwQMJ7zstKJcgiteGYnFKI%2FlIIdcxzvlbHvVDzvYbX%2Fxy7267VgbDzLB4nHdt09b93sAkdVOGHlV8HKR8lOSHUiGDaU3EBUirVTFQJ%2FPW2jgnFw9tZCtoMotVYFGDE5NiG%2BpHI79wJZeNPrTzx2H58xZ9NBjAKZmPVEj6COg9uof0O9ul3LcUTCBoszTU4KfXWiVmxEAGQlbvhIe%2Fx8gH1O0brVd7mwBi%2F7Aihc3WKo6LEiVsMDfD%2F0kVKLaadBdKOeXjqgtsGDQVMRb0vLa7BO%2BdanXyzM7OIkPKAqFYQdUsTlXjs5HIGWkdoup1qLhtYSV9NNJl2wVt%2BbnYJvVX151j1cGNPh4M9Ru8g50gNdO6vpOFMHswyxXx21xG82y0qppMQl9aP83BCR10Io2PyX9jLxKP2GAoH%2Fd6nT7HY%2F8%2FBwpp7KiHSw1Ivm1RAlXWQ8XWjFgqT%2Bt7VBEo2KVy7SJ4U%2FvuxR0AhmLSry2qwWPK0Y9WWe3NqOHOWrKgph1hJOtXB7XMm5aiIkwdlnmoaTd3SC%3D%22%2C%22e%22%3A%22X4RaP3u42PE1-YReTopVjYB5tRwHtVY4Xqw8jXDNEjuOu02fmTbbQ8TJwo5S8wQyxFTeobcgqh4RB6SlJnz3dfhP9_15dpnrtSqJnvya92AqwVDaHNZgpMg_4xpYvsTMEAm48ZHXJRNfarQNwp4bK18BgcdcMWlkaHP8A7SabYfqGNa_W30Dd3IxG7FCr7yBEXMT5H0wOHYcrpUd-8MBIZ4IKNYdh5ElOOURlWM9mtU%22%7D"
#   }

# response = requests.post('https://passport.simuwang.com/index.php/auth/login', headers=headers, cookies=cookies, data=data)
# 　　#登录的URL
#     baseurl += "/login/email"
# 　　#requests 的session登录，以post方式，参数分别为url、headers、data
# baseurl = "https://passport.simuwang.com/index.php/auth/login"
# content = session.post(baseurl, headers = login_headers, data = login_data)
# print(content.cookies)  
# # response = session.post('https://ppwapi.simuwang.com/ranking/company', headers=headers, cookies =content.cookies,  data=data)
# response = session.get("https://dc.simuwang.com/company/CO0000031J.html")
# print(response.text)
# response = json.loads(response.text)
# for index,data  in enumerate(response['data']['list']):
#     # print(data["company_id"])
#     # print(data["company_name"])
#     # print(data["corestrategy"])
    
#     print(data["ret"])
#     # print(data[""])
    





# curl 'https://ppwapi.simuwang.com/ranking/company' \
#   -H 'Connection: keep-alive' \
#   -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"' \
#   -H 'Accept: application/json, text/plain, */*' \
#   -H 'Content-Type: application/x-www-form-urlencoded' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46' \
#   -H 'sec-ch-ua-platform: "Windows"' \
#   -H 'Origin: https://dc.simuwang.com' \
#   -H 'Sec-Fetch-Site: same-site' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Referer: https://dc.simuwang.com/' \
#   -H 'Accept-Language: zh-TW,zh-HK;q=0.9,zh;q=0.8,en;q=0.7,zh-CN;q=0.6,en-GB;q=0.5,en-US;q=0.4' \
#   -H 'Cookie: sajssdk_2015_cross_new_user=1; Hm_lvt_c3f6328a1a952e922e996c667234cdae=1648023754; qualified_investor=0; focus-certification-pop=1; need_update_password=1; smppw_tz_auth=1; certification=1; evaluation_result=4; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217fb65d759536b-00334f14191865-5617185b-1327104-17fb65d75961249%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217fb5ded2331db-074ccf990dfe15-5617185b-1327104-17fb5ded234123b%22%7D; Hm_lpvt_c3f6328a1a952e922e996c667234cdae=1648032054' \
#   --data-raw 'page=3&sort_name=ret&sort_asc=desc&condition=ret%3A4%3B&USER_ID=1830378' \
#   --compressed


## Login
# curl 'https://passport.simuwang.com/index.php/auth/login' \
#   -H 'Connection: keep-alive' \
#   -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"' \
#   -H 'Accept: application/json, text/plain, */*' \
#   -H 'Content-Type: application/x-www-form-urlencoded' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46' \
#   -H 'sec-ch-ua-platform: "Windows"' \
#   -H 'Origin: https://dc.simuwang.com' \
#   -H 'Sec-Fetch-Site: same-site' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Referer: https://dc.simuwang.com/' \
#   -H 'Accept-Language: zh-TW,zh;q=0.9' \
#   -H 'Cookie: sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217fb6f67275705-09da17c61c4e73-5617185b-1327104-17fb6f6727686d%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217fb6f67275705-09da17c61c4e73-5617185b-1327104-17fb6f6727686d%22%7D; Hm_lvt_c3f6328a1a952e922e996c667234cdae=1648042079; PHPSESSID=t8dluq8m9rb1fj6o9jski64742; Hm_lpvt_c3f6328a1a952e922e996c667234cdae=1648044795' \
#   --data-raw $'username=15773211225&password=Lyp82nlf&do_qualified=1&reme=1&NVCVal=%257B%2522a%2522%253A%2522FFFF0N00000000008289%2522%252C%2522c%2522%253A%2522FFFF0N00000000008289%253Anvc_register%253A1648044796545%253A0.4660441376863911%2522%252C%2522d%2522%253A%2522nvc_register%2522%252C%2522j%2522%253A%257B%2522test%2522%253A1%257D%252C%2522h%2522%253A%257B%257D%252C%2522b%2522%253A%2522221\u0021uMCu%252BIi9qS0chCg1gpHzzjVj8GURUdF03na%252Bfg%252FPfYFGWmfyw7te5uNtL1dt7HTnmB2qriGap6uibZatZByew3So%252FM5PJzhnp2EGlvWxsUJ5elUFNrvXOidJfdbAN8xWFMQkG9vtnXPE6J7dOHx56gdHaVPVrZw%252BNyKWh9GqE0tap3hMrSpz7Z0o0L6RvKE96mujTy98t1FWhcHW2olqfdtc6gZP2BxlONaNm5HDpySHDC8oX%252BYQGi4A6qdxqg6oYA3lNIofcpo8RN5pV%252Bx63pYeZjRET1SiTSH%252Fb4Lh6iD3c%252F4Y5D0lo9TWl3YgHXnxJfXnn3ZcqYgCy%252FzOq6pBbfnmK4leQ4a6%252FzJm00rMuWpqBtgZIvv%252FsA2SwJfHsh1sk84h%252FqGMB4u0KHwL3PZ3a4DmZ6hlB5u1%252FYksMv74iqvBs%252FaMVYIvZZoQ%252B5NeWImEtPwwgDfw8e9A7rroNQVNOiTeKiSSQVEw7aN6kYYobx0RyaEeywB76QQmJccm4SIZeIbFwkVRcEP2CWyVMDHggADRW%252BA7vgFEq%252FWDEUI%252BSKPG9bxfuaiR8id%252F5OZ%252Ba2w3qHs40gU95qkNOjTutrvMjgsNdLyWZpw5iSPsGA5sCofwgSBrTApnE79PKLCNX%252BTg9mY7t3279nKiwAox1oZKuR1Lg4lruhGYLBZCGvzqfov%252Fy8gp2RoVv41UDvZVY5di20RcLL6RoQOqeEbdcd7UGA6pc6%252B6T9KQ9TfOYx%252BnZ3n9VZ5qeCd7yiEXq%252Fs5xv8yJpWo44vn6UTt7fBDiqDlT4npQI6N81jorhdxQ4HsQI19Lg6i8v1ZlDjgtinUzQ1AysW77pt5OQrJJpTAeAsMd%252FM3oy1Az2J97RVowD2gb3UXOHvZ5mgq57SIAldh9oCvPqyZ8DOUGYO7ryo18Ttu%252Fnm%252B%252FnFEMbaDbuCc48WbtHGopO6p%252B2n%252Bas3Iv2bE0Mh%252Bvs%252FOSmMrhOELuP%252FqMHPJqo7khSlKc2%252BZBrNvoT6vzQpcYEEJp%252FOOrQOBFE5kpgHw2nvK37Z0XD9Y8Xk1nG5mOWaYms90nA6R9RVC%252BXiTvHJAab5CFuN%252BWtyyP%252FcGiz%252F0of8xl8JYytj04eVny2F%252FL40%252Faukuq5JXdTGrna8FyuGKOxnZyWHFcXEk%252FnCgeijYcLfUqQmHC6TFfyhkm%252FzffbEMVIknFMkUUb7GRSEa4SSa2CrpDNcztle%252B3WL42dAMnE4e1K6Omqw4kXePYYhQV05x3ixgirNieWIdYek0swEFW5D9IPhO5T8gA0YX93KeOk3H2WHXlRHeLgFYZKGgYWyntAhIfyc0dCukDitgijDq9e%252FOVM73wHrkDuaRGugVgfeMFJqbJmgZ%252B1w2mz4dM9HlAicV9RJmQZm1Kcqmvzz8UCeBpvHlJiO1aUQ99lMR6LLHFJmtdcQ9zH5vlLy6jhfMKEPweXU1UJ9b3EKcYh63pxvjBy8%252FIHmy7ybIq3BwMZk3U2VsL8cwyP6SiHly%252BvJOMHwghd8lytfxd8ULs9y4tVaqtjumZ9mJ3P4xvvgb1vIweEhNHkcqx%252FjSXeMS1sUgFKq6kCapE%252B2UNPOVWffOLlfVZJrrrAh%252FJCUaLzwXL%252BmUatvkAk5mp5ncqg%252FNc3g6aV0lIZlUQn5%252FJIQtDz4zf83cKkpOtUzdE1mpe8fqz0SWMi7OcA%252BT5Im5tWOQ7ikMNBjs13ip7nJAXRYYX7rG2pn2%252BJnNQKh4BZa0MPLEujqgRR179HruhUNtKqLbvildICy%252FyBLM7AgLkH10h9lvhJ9Af%252BKUV%252BamHYwGeM4Uw7UZVbc2lZRtwJZb2k30Nj6m5RHzcG7GM0vN%252F8ujyJcA%252BzmvVPkGgwonmdcRWmYBJ%252Bt2M7QpOHvrHSf6usvNDCBJYMyxls44ik0n94f3%252BXcQfJLBL16BxsW7tmeN%252BTDwtfTRx3XRz0WqYc7FDgaEhEECgEaP4ocZsylwe0x%252BC19glza8tD7FfIj37up%252FI8BwYl51sLuRORW6lXXDqpuPn20kdz%252FBFKp8uBVZ8844iM1OyQun6YL3heusTTCbH8qlqF3ZNOl6MEHxihnmdPMIqB%252BxqOS7fNuB%252FUU4fPT6u12DK87v4%252F3DvweURqv%252Btquio5N38MyL8SGfacrkimgFv9oiGH1vUbsDL%252BGkhNZBlpNkhavAgUI3ToeAUwaxxxxDLR1p5oQ%252F68C0l%252BBCzGYRYTy5Lhi0jeKyybSsV5tfVqrAf8oCw1T7vpn96lWd0Zp79Kw9HKuNt7uJocLA%252BKKok5DGHkbJwwmCC4WL4O%252BUauY1ayn8oKsrW2XO3kPKM0whPNzkdhjNcLj2ZgnKNxxC2FXIjj50oh6o4X9E36DPHWHEPMPY0ARzcFJB2J5wVhRgi3rdRMVVQD4GD74e6GD1xvh6Sm3GQsN%252BvQ%252F7wIYpo6CcVz2x4V9ICs6ft7gT0N4rw3DgjlVOQGoOxbCsCCge5Z%252F%252Fan2BpPxjpVlZ6Quf0ZOioCNujal%252BjMiLSC5iLZ7zfeYD97qNZKsFTg1Nr7vggLFXu3cv57ynzJ6V40tTxHUmYXs3bamqUawwZ5sIyCpqkfoSowx%252BkGTUHI%252BZhwTEvW5aaU40c0Ng4Lb1q%252BoQWQdbcvvAUavKcWFJcmoSI81jrge4RsMGxjcpPOmhUcLfgyCJTuedJVmFJxE8QOQ3wXCr44MhZy419mpN3%252B%252BbRi9HgjoaLJOCT4g4nrPatnNt9f9BIcEpCrlqdyIieXLWNkQAtN6H1dwxmn%252B7V1IXRAz0L1Aa1wzvsGxg%252FouLGDn17GAngFU1%252ByCyt9LoeonQtWGrMYy%252B%252FeEC2q%252Ba64z7DPP42hl8tHtt%252BYvonEWIb24%252F4Gr8DCIoz2g4bVPefDLfXddsqKeUw5%252BeNlFZYrCZf7dlbYFfdfnlVEQZheiOInSj8QH5scZM6ium1bqfO0iLEvDHVhLGXrFm0tqBFkbu4f4sm9K4kd0Ky8o9KwROVhtfQKNUvcldIpJ5X46rKYttySpUK2q4MxizK6UCZmDCuvf96yd8dw%252FjGfvjb1EFnAhMzAwC5CbEQfUOoixwNYaIRdoB3TRClbY6NpYoHl2Qy%252B3ZtveUwutDugtEMBjJXs1wzGbIgd0B48dE3fMYRp3UL%252FlncSLDKAgRP6xHJO5lzIo2hdEw6L17via9Bjulg9e%252B3T%252FVjS0PgcyqF%252BQ9b3FzEdbqi9ZB0ZHY3UZ0b47rbffoH2XiDA0pU0m7wph7FZE3PRocOjDHTMu5vVs6cq7E4UpIonmAX1EV%252F07tkUgN3g7ApK3RTiu6ojrUk7fU%252FiyfrK%252BT3EkOpF5uxQeSBxwmUow6Kb1pub7xuPWt5V%252FmvqJKVzfDR4sPNrX4KpkG3J2s50BnM%252BLrZ9%252FjOuTq3UGvXvfWVWzML%252BRX2FsMhSlVP7wVog0JtVPSlhwVGundNkJXC0hmF8vhgBKC5bJfSxMZtWTZ07hg6L0%252Fp1HJE%252Bry5gmYCIsKe2p4keMMx0Gh%252FFBlyC18%252Bq2tcOy0E3S%252BZ2%252FFZvrRDZWkbFkAPowR1oLDmL54WWerAXKDbR%252FRFp1ACvXYIUak3gSyk5Rhz7GnuAbBmSaBs60D%252FTaB3s%252FrVuz58Mz5CEhnuA85dfHACZ1%252FWDqKDVhjMu1rb4QNAXr5WxCHMv8ZCklGU8zpngytcY7aVyCSXhYXfipGNsT2Yq9e%252BOwxHTGCBCUoIpqa%252BGvwF%252BpNWuzOXK7%252FnzjIGQYRJWFu%252FWHXkMcXWU4zuDjeDvrBtzuCLVD%252FVRdcsJ9h2G4fNdmVSUYe2p1yYhwl7TJqh29LtZtgc1u2l76K9WtySnMpxrEklcIw%252F7yBBuG7XeXIJkEWiphM6O2DvHJgh9vOKLPSFvkcrknDIIa5TB8dMrEturE6MbUWG9JEKTL1y66U4IDL8FXepU%252FjCt98vbVeDQBMBwsfFCX25v9zH8wYXEqbFF1aNdyi7fvFccAFUepiXXWG9u%253D%253D%2522%252C%2522e%2522%253A%2522X4RaP3u42PE1-YReTopVjYB5tRwHtVY4Xqw8jXDNEjuOu02fmTbbQ8TJwo5S8wQyxFTeobcgqh4RB6SlJnz3dfhP9_15dpnrtSqJnvya92AqwVDaHNZgpMg_4xpYvsTMEAm48ZHXJRNfarQNwp4bK18BgcdcMWlkaHP8A7SabYfqGNa_W30Dd3IxG7FCr7yBEXMT5H0wOHYcrpUd-8MBIZ4IKNYdh5ElOOURlWM9mtU%2522%257D' \
#   --compressed