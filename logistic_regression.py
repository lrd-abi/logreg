import pandas as pd 
import numpy as np 
import math

cc= pd.read_csv("it_churn.csv")

cc["gender"]=cc["gender"].replace({"Male":1,"Female":0})
cc["Partner"]=cc["Partner"].replace({"Yes":1,"No":0})
cc["Dependants"]=cc["Dependants"].replace({"Yes":1,"No":0})
