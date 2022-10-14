import boto3
from botocore.exceptions import ClientError
import json
import os
from typing import Union
import requests
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware  #引入 CORS中间件模块

app = FastAPI()
#设置允许访问的域名
origins = ["*"]  #也可以设置为"*"，即为所有。

#设置跨域传参
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  #设置允许的origins来源
    allow_credentials=True,
    allow_methods=["*"],  # 设置允许跨域的http方法，比如 get、post、put等。
    allow_headers=["*"])  #允许跨域的headers，可以用来鉴别来源等作用。

class A:
    email = 'cloudflare_account_email'
    key = 'cloudflare_account_api'
    zone = 'cloudflare_account_zone'
    ddns_url = 'ddns_domain_name'

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

ec2 = boto3.client('ec2')

instance_id =  os.getenv("INSTANCE_ID", default=None) # change this {INSTANCE_ID} INSTANCE_ID={INSTANCE_ID}

class IP:

    def __init__(self,ins_id):
        self.public_ip = ""
        self.allocation_id = ""
        self.instance_id = ins_id
        self.filter = None

        #self.get_information()

    def display(self):
        print(self.public_ip)
        print(self.allocation_id)

    def set_filter(self,name='domain',value='vpc'):

        self.filter =[
                {
                    'Name': name,
                    'Values': [value]
                    }
                ]

    def associate_ip(self):
        allocation = ec2.allocate_address(Domain='vpc')
        response = ec2.associate_address(AllocationId=allocation['AllocationId'],InstanceId=self.instance_id)

    def get_information(self):

        response = ec2.describe_addresses(Filters=self.filter)
        print(response)
        aws_info = response['Addresses']
        for ii in aws_info:
            if len(ii)==10:
                print(ii['InstanceId'])
                print(ii['PublicIp'])
                return ii['InstanceId'],ii['PublicIp']

    def release_ip(self):

        response = ec2.describe_addresses(Filters=self.filter)
        print(response)
        aws_info = response['Addresses']
        for ii in aws_info:
            if len(ii)==5:
                aws.public_ip = ii['PublicIp']
                aws.allocation_id = ii['AllocationId']
                #aws.display()
                print(aws.public_ip + " releases\n")
                ec2.release_address(AllocationId=aws.allocation_id)

try:

    aws = IP(instance_id)
    aws.set_filter()
    aws.get_information()


except:
    #print("Please input instance_id")
    print(":)")

@app.get("/get_ip")
def read_root():
    aws.set_filter()
    _,ip = aws.get_information()
    return {"Server": ip}


@app.get("/change_ip")
def read_item(name: str,value:str):
    if value == 'y':

        _ , aa_old = aws.get_information()

        aws.associate_ip()
        aws.release_ip()
        _delete_dns()
        _ , aa = aws.get_information()

        json_data['content'] = aa
        json_data['name'] = _cf.ddns_url
        response = requests.post(url, headers=headers, json=json_data)

        return {"New server":aa,"Delete server":aa_old,"Domain":_cf.ddns_url}