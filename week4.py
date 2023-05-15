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
for i in range(1,21):#1,21 normal #11
    target=date(today.year-i,today.month,today.day)
    #if target.weekday()<5:
    for j in range(0,target.weekday()):
        print(" ",end="")
    for j in range(0,366):
        k=datetime.strftime(target+timedelta(days=j),'%Y/%m/%d')
        l=datetime.strftime(target+timedelta(days=j+7),'%Y/%m/%d')
        if k in dc.keys() and l in dc.keys():
            src=float(dc[k].replace(',',''))
            dst=float(dc[l].replace(',',''))
            print('+'if src<dst else'-'if src>dst else'=',end="")
        elif k in dc.keys():
            for n in range(1,9):#fixed 9days
                l=datetime.strftime(target+timedelta(days=j+7+n),'%Y/%m/%d')
                if l in dc.keys():
                    src=float(dc[k].replace(',',''))
                    dst=float(dc[l].replace(',',''))
                    print('+'if src<dst else'-'if src>dst else'=',end="")
                    break
        else:
            if (target+timedelta(days=j)).weekday()<5:
                print(" ",end="")
    print("")
