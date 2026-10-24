import pandas as pd 
import numpy as np 




def clean():
    cc= pd.read_csv("it_churn.csv")
    

    cc["Churn"]=cc["Churn"].replace({"Yes":1,"No":0}).astype(int)
    cc["gender"]=cc["gender"].replace({"Male":1,"Female":0}).astype(int)
    cc["Partner"]=cc["Partner"].replace({"Yes":1,"No":0}).astype(int)
    cc["Dependents"]=cc["Dependents"].replace({"Yes":1,"No":0}).astype(int)
    cc["MultipleLines"]=cc["MultipleLines"].replace({"Yes":1,"No":0,"No phone service":2})
    cc["OnlineSecurity"]=cc["OnlineSecurity"].replace({"Yes":1,"No":0,"No internet service":2})
    cc["OnlineBackup"]=cc["OnlineBackup"].replace({"Yes":1,"No":0,"No internet service":2})
    cc["DeviceProtection"]=cc["DeviceProtection"].replace({"Yes":1,"No":0,"No internet service":2})
    cc["StreamingTV"]=cc["StreamingTV"].replace({"Yes":1,"No":0,"No internet service":2})
    cc["StreamingMovies"]=cc["StreamingMovies"].replace({"Yes":1,"No":0,"No internet service":2})
    cc["PhoneService"]=cc["PhoneService"].replace({"No":0,"Yes":1}).astype(int)
    cc["Contract"]=cc["Contract"].replace({"Month-to-month":0, "One year":1, "Two year":2})
    cc["PaperlessBilling"]=cc["PaperlessBilling"].replace({"Yes":1,"No":0}).astype(int)
    cc["PaymentMethod"]=cc["PaymentMethod"].replace({"Electronic check":1,"Mailed check":2,"Bank transfer (automatic)":3,"Credit card (automatic)":4})
    cc["InternetService"]=cc["InternetService"].replace({"DSL":1,"No":0,"Fiber optic":2})
    cc["TechSupport"]=cc["TechSupport"].replace({"Yes":1,"No":0,"No internet service":2})


    cc["TotalCharges"]=pd.to_numeric(cc["TotalCharges"],errors="coerce")
    cc=cc.dropna()
    

    cc=pd.get_dummies(cc,columns=["MultipleLines",'InternetService','OnlineSecurity','OnlineBackup',"DeviceProtection",'TechSupport','StreamingTV','StreamingMovies','Contract',"PaymentMethod"],drop_first=True,dtype=int)

    return cc



   
    



