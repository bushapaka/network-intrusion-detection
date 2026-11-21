import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv('clean_data.csv')
df['label'].value_counts().plot(kind='bar',color=['green','red'])
plt.title("Normal vs Attack")
plt.savefig("result.png")
print("Graph Ready!")