import pandas as pd

n=['nitin','raman']
g=['male','male']


df = pd.DataFrame(data= {'name':n,'gender':g})


print(df)

df.to_csv(r"C:\Users\vkumar15\Desktop\backup\mydata.csv")
