import pandas as pd

ck=pd.read_csv("it_churn.csv")

x=ck.nunique()

y=ck.apply(pd.unique)
print(y)
