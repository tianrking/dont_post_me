import pandas as pd


df = pd.read_csv('final_with_url.csv')
print(df.describe())
print(df.shape)
# print(df.head(2))
print(df.columns)