## ec2 配置 

```bash
pip install -r requirtments.txt
```

{Region} us-east-1 us-east-2

{State} running 

https://{Region}.console.aws.amazon.com/ec2/home?region={Region}#Instances:instanceState={State}

```bash
instance_id = xxxx  執行個體 ID
```


```bash
aws configure
```

## cloudflare 配置 

修改 22-26行 为自己的 cf 账户 api 和 zone

```bash
email = 'cloudflare_account_email'
key = 'cloudflare_account_api'
zone = 'cloudflare_account_zone'
ddns_url = 'ddns_domain_name'
```

## 运行

```bash 
INSTANCE_ID=$INSTANCE_ID uvicorn ec2_changeip:app --reload --host 0.0.0.0
```

or

```bash 
INSTANCE_ID=$INSTANCE_ID uvicorn ec2_ddns:app --reload --host 0.0.0.0
```

访问 x.x.x.x:port/get_ip  得到当前服务器ip
访问 x.x.x.x:port/change_ip?value=y&name=1  随机修改服务器 ip 并自动修改dns记录 到 ddns_url

- API 

    - x.x.x.x:port/get_ip
    - x.x.x.x:port/change_ip?value=y&name=1