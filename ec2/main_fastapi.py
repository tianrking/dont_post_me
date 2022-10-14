import boto3
from botocore.exceptions import ClientError
import json
import os
from typing import Union

from fastapi import FastAPI

app = FastAPI()

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
    
    aws = IP(instance_id) instance_id
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
        
        _ , aa = aws.get_information()
        return {"New server":aa,"Delete server":aa_old}
