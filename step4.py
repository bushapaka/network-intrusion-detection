import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
df=pd.read_csv('clean_data.csv')
x=df.drop('label',axis=1)
y=df['label']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model=RandomForestClassifier()
model.fit(x_train,y_train)
print("Model Training Done!")
print("Accuracy:",model.score(x_test,y_test))
      



 
