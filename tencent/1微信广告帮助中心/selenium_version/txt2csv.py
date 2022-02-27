from pickle import NONE
from nbformat import read
import pandas as pd

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)

read_file = pd.read_csv (r'/home/tianrking/pachong/app/ad_weixin_qq_com_guide_titile_clean.csv',engine = "python",header=None,
                 names=['KEY', 'URL'])
print(read_file[read_file['KEY']=='相关问题'])
read_file = read_file[read_file['KEY']=='相关问题']
read_file.to_csv(r'/home/tianrking/pachong/app/相关问题.csv')