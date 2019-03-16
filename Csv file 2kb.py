import pandas as pd
import random
import os
num=1
sofi=["Num1","Num2","Num3","Num4","Num5"]
new=pd.DataFrame([],columns=sofi)
def csv(file):
    new.to_csv(file)
    #global n
    a=1
    while os.stat(file).st_size<2000:
        n=[random.randint(1,100) for i in range(len(sofi))]
        n.insert(0,a)
        a=a+1
        n=pd.DataFrame([n])
        n.to_csv(file, mode='a',header=False,index=False)
while num<=3:
    file="filee"+str(num)+".csv"
    csv(file)
    num=num+1
