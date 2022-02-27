from traceback import print_tb
import pandas as pd
import json
# df = pd.read_csv('QA.csv',set_index=['0','Q','A'])
# df = pd.read_csv('QA.csv')

file = 'QA.csv'
df = pd.read_csv(file,names=['0','Q','A'])
df = df[['Q','A']]


# print(df.shape[0])
# print(df.describe)
# print(df.head())

for _index in range(0,df.shape[0]):
    chaos_data = json.loads(df['A'][_index])
    # print(chaos_data.keys())
    chaos_data = chaos_data['content']

    # print(chaos_data)
    
    clean_data = []
    for gg in chaos_data:
        try:
            clean_data.append(gg['content'])
            # print(gg['content'])
        except:
            # pass
            continue
    print(clean_data)
    # try:
    #     question = df['Q'][_index]
    #     # print(question,clean_data)
    #     df = pd.DataFrame(data=[
    #             [question,clean_data]],
    #             columns = ['Q','A'],
    #             )
    #         # df = 
            
    #     df.to_csv('QA_clean.csv', mode='a',header=False)
    #     print(clean_data)
    # except:
    #     continue
    