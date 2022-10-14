## 

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

```bash 
INSTANCE_ID=$INSTANCE_ID uvicorn main_fastapi:app --reload --host 0.0.0.0
```

- API 

    - x.x.x.x:port/get_ip
    - x.x.x.x:port/change_ip?value=y&name=1