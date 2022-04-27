import pandas as pd
import json

with open("data_all.json",'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)

item = load_dict['data']['posts']['rows']

for i in range(0,len(item)):
    df = pd.DataFrame()
    Q = item[i]['post_title']
    A = item[i]['post_data']
    
    df = pd.DataFrame(data=[
                    [Q,A]],
                    columns = ['Q','A'],
                    )
    df.to_csv('data_all_in_one/QA.csv', mode='a', header=False)
    print(i)
    