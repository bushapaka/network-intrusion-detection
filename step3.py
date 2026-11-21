import pandas as pd
df=pd.read_csv('network_logs.csv')
df=df[['dur','sbytes','spkts','dbytes','proto','label']]
print(df.isnull().sum())
df['proto']=df['proto'].astype('category').cat.codes
df.to_csv('clean_data.csv',index=False)
print("Cleaning Done!")