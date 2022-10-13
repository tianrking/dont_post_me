import boto3
from botocore.exceptions import ClientError
import json
import os

ec2 = boto3.client('ec2')

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
     #       if len(ii)==5:
     #          aws.public_ip = ii['PublicIp']
     #          aws.allocation_id = ii['AllocationId']
     #          print("releases")
     #          print(aws.public_ip + " releases\n")
            if len(ii)==10:
                print(ii['InstanceId'])
                print(ii['PublicIp'])

try:
    instance_id = "Your ec2 id"
    aws = IP("i-05f47f33b9bef9fe5")
    #aws = IP(str(instance_id))
    aws.associate_ip()

except:
    print("Please input instance_id")

try:
    
    #allocation = ec2.allocate_address(Domain='vpc')
    #response = ec2.associate_address(AllocationId=alloication['AllocationId'],InstanceId=aws.instance_id)


    filters = [
        {'Name': 'domain', 'Values': ['vpc']}
    ]
    
    response = ec2.describe_addresses(Filters=filters)
    #print(response)
    aws_info = response['Addresses']

    for ii in aws_info:
        if len(ii)==5:
            aws.public_ip = ii['PublicIp']
            aws.allocation_id = ii['AllocationId']
            #aws.display()
            print(aws.public_ip + " releases\n")
            ec2.release_address(AllocationId=aws.allocation_id)
        if len(ii)==10:
            print("Now is " + ii['InstanceId'] + " " + ii['PublicIp'] )

except ClientError as e:
    print(e)


