import pandas as pd

df = pd.read_csv('QA_clean.csv')
df = df.drop_duplicates()
print(df.head(10))
