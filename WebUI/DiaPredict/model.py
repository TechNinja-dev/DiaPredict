import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer
import joblib


df=pd.read_csv("C:/Users//Lucifer/Desktop/My Git Repos/DiaPredict/Dataset of Diabetes.csv")

df.drop(columns=['ID'],inplace=True)   #removing unnessecery features
df.drop(columns=['No_Pation'],inplace=True)   #removing unnessecery features
LE=LabelEncoder()
cols=['Gender','CLASS']                                     #F-0 M-1 f-2
for i in cols:                                              #N-0   N'-1  P-2 Y-3 Y'-4
    df[i]=LE.fit_transform(df[i])
    # for index, label in enumerate(LE.classes_):
    #     print(f"{label} → {index}")
    
x=df.iloc[:,:-1]   #seperating independent and dependent variables
y=df.iloc[:,-1]

x_train,x_test,y_train,y_test=tts(x,y,test_size=0.3,random_state=4)  #splitting dataset into training and testind data

svm=SVC()                 #training svm model
svm.fit(x_train,y_train)
y_pred=svm.predict(x_test)
# print(accuracy_score(y_test,y_pred))  0.84

joblib.dump(svm,"Predictor.joblib")

# 'Gender', 'AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG','HDL', 'LDL', 'VLDL', 'BMI']
def predict(g,a,u,cr,hb,ch,tg,hdl,ldl,vldl,bmi):
    import joblib
    tell=joblib.load("Predictor.joblib")
    res=tell.predict(np.array([[g,a,u,cr,hb,ch,tg,hdl,ldl,vldl,bmi]]))
    return res
