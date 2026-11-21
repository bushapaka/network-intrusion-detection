import pandas as pd 
df= pd.read_csv('network_logs.csv')
print(df.head())
print(df.shape)
print(df['label'].value_counts())

