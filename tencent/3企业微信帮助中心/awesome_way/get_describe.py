import pandas as pd

import pandas as pd
import os

c_dir = 'data_all_in_one'
files = os.listdir(c_dir)
for i in files:
    try:
        df = pd.read_csv(c_dir+"/"+i)
        # print(df.describe())
        print(df.shape)
    except:
        continue