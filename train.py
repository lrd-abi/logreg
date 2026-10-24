import pandas as pd
import numpy as np
from cleaner import *


pr=clean()
print(pr.dtypes)
rng = np.random.default_rng(42)

train_idx,test_idx= [],[]

for label in pr["Churn"].unique():
    idx=rng.permutation(pr.index[pr["Churn"]==label].to_numpy())
    cut=int(0.7*len(idx))
    train_idx.extend(idx[:cut])
    test_idx.extend(idx[cut:])

train_df= pr.loc[train_idx].sample(frac=1,random_state=42)  
test_df= pr.loc[test_idx].sample(frac=1,random_state=42)  


scaled_train=[]
mean_train=[]
std_train=[]

TotalCharges=np.array(train_df["TotalCharges"])
MonthlyCharges=np.array(train_df["MonthlyCharges"])
tenure=np.array(train_df["tenure"])

x=[TotalCharges,MonthlyCharges,tenure]

for i in x:
    mean=np.mean(i)
    std=np.std(i)
    scaled_train.append((i-mean)/std)
    mean_train.append(mean)
    std_train.append(std)

train_df["TotalCharges"]=scaled_train[0]
train_df["MonthlyCharges"]=scaled_train[1]
train_df["tenure"]=scaled_train[2]

scaled_test=[]

TotalCharges=np.array(test_df["TotalCharges"])
MonthlyCharges=np.array(test_df["MonthlyCharges"])
tenure=np.array(test_df["tenure"])

x=[TotalCharges,MonthlyCharges,tenure]

for j,i in enumerate(x):
    scaled_test.append((i-mean_train[j])/std_train[j])


test_df["TotalCharges"]=scaled_test[0]
test_df["MonthlyCharges"]=scaled_test[1]
test_df["tenure"]=scaled_test[2]  
