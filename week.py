#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
from datetime import datetime,date,timedelta
import csv
dc={}
with open("0.csv", newline="") as f:
    for d in csv.reader(f):
        dc[d[0]]=d[4]
today=date.today()
if len(sys.argv)>1:
    a=int(sys.argv[1])
    today=today-timedelta(days=-a) if a<0 else today+timedelta(days=a)
yer=today.year
mon=today.month
day=today.day
x=today.weekday()
for i in range(1,11):#1,21 normal
    target=date(yer-i,mon,day)
    y=target.weekday()
    d=x-y-7 if x-y>3 else 7+x-y if y-x>3 else x-y
    target=target+timedelta(days=d) if d>0 else target-timedelta(days=-d)
    b=mx=mn=rate=0
    for j in range(0,8):#0,8 normal #0,12gd
        k=datetime.strftime(target+timedelta(days=j),'%Y/%m/%d')
        if k in dc.keys():
            dck=float(dc[k].replace(',',''))
            if b==0:
                mn=mx=b=dck
                print(k,end=" ")
            else:
                print('-' if b>dck else '+' if b<dck else '=',end="")
                if dck>mx:
                    mx=dck
                elif dck<mn:
                    mn=dck
    print("")
    lx=[]
    ly=[]
    xx=0
    rate=mx-b if mx-b>b-mn else b-mn
    if rate!=0:
        for j in range(0,8):#0,8 normal #0,12gd
            k=datetime.strftime(target+timedelta(days=j),'%Y/%m/%d')
            if k in dc.keys():
                lx.append(xx)
                xx+=1
                ly.append((float(dc[k].replace(',',''))-b)/rate)
        plt.plot(lx,ly)
        plt.text(i%xx,ly[i%xx],"{}:{}".format(target.year,str(rate)))
plt.show()
