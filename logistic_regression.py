import pandas as pd 
import numpy as np 
import math

cc= pd.read_csv("it_churn.csv")

cc["Churn"]=cc["Churn"].replace({"Yes":1,"No":0})
cc["gender"]=cc["gender"].replace({"Male":1,"Female":0})
cc["Partner"]=cc["Partner"].replace({"Yes":1,"No":0})
cc["Dependents"]=cc["Dependents"].replace({"Yes":1,"No":0})
cc["MultipleLines"]=cc["MultipleLines"].replace({"Yes":1,"No":0,"No phone service":2})
cc["OnlineSecurity"]=cc["OnlineSecurity"].replace({"Yes":1,"No":0,"No internet service":2})
cc["OnlineBackup"]=cc["OnlineBackup"].replace({"Yes":1,"No":0,"No internet service":2})
cc["DeviceProtection"]=cc["TechSupport"].replace({"Yes":1,"No":0,"No internet service":2})
cc["StreamingTV"]=cc["StreamingTV"].replace({"Yes":1,"No":0,"No internet service":2})
cc["StreamingMovies"]=cc["StreamingMovies"].replace({"Yes":1,"No":0,"No internet service":2})
cc["PhoneService"]=cc["PhoneService"].replace({"No internet service":2,"No":0,"Yes":1})
cc["Contract"]=cc["Contract"].replace({"Month-to-month":0, "One year":1, "Two year":2})
cc["PaperlessBilling"]=cc["PaperlessBilling"].replace({"Yes":1,"No":0})
cc["PaymentMethod"]=cc["PaymentMethod"].replace({"Electronic check":1,"Mailed check":2,"Bank transfer (automatic)":3,"Credit card (automatic)":4})
cc["InternetService"]=cc["InternetService"].replace({"DSL":1,"No":0,"Fiber optic":2})
cc["TechSupport"]=cc["TechSupport"].replace({"Yes":1,"No":0,"No internet service":2})




cc=pd.get_dummies(cc,columns=["MultipleLines",'InternetService','OnlineSecurity','OnlineBackup',"DeviceProtection",'TechSupport','StreamingTV','StreamingMovies','Contract',"PaymentMethod"],drop_first=True,dtype=int)

scaled=[]
cc["TotalCharges"]=pd.to_numeric(cc["TotalCharges"],errors="coerce")

TotalCharges=np.array(cc["TotalCharges"])
tenure=np.array(cc["tenure"])
MonthlyCharges=np.array(cc["MonthlyCharges"])

x=[TotalCharges,tenure,MonthlyCharges]

scaled=[]

for i in x:
    mean= np.nanmean(i)
    std=np.nanstd(i)
    scaled.append((i-mean)/std)

cc["TotalCharges"]=scaled[0]
cc["tenure"]=scaled[1]
cc["MonthlyCharges"]=scaled[2]

    
print(cc.apply(pd.unique))



