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
buf=[]#fixed length(29)
for i in range(1,21):#1,21 normal #11
    target=date(today.year-i,today.month,today.day)
    m=0
    for j in range(0,365):
        k=datetime.strftime(target+timedelta(days=j),'%Y/%m/%d')
        l=datetime.strftime(target+timedelta(days=j+7),'%Y/%m/%d')
        if k in dc.keys() and l in dc.keys():
            if int(k[5:7])!=m:
                if m!=0:
                    print(''.join(buf)+str(int(k[5:7])),end="")
                m=int(k[5:7])
                buf=list('                         ')
                x=date(today.year-i,m,1).weekday()
                bufi=0 if(x==5 or x==6)else x
            src=float(dc[k].replace(',',''))
            dst=float(dc[l].replace(',',''))
            buf[bufi]='+'if src<dst else'-'if src>dst else'='
            bufi+=1
        elif k in dc.keys():
            for n in range(1,9):#fixed 9days
                l=datetime.strftime(target+timedelta(days=j+7+n),'%Y/%m/%d')
                if l in dc.keys():
                    if int(k[5:7])!=m:
                        if m!=0:
                            print(''.join(buf)+str(int(k[5:7])),end="")
                        m=int(k[5:7])
                        buf=list('                         ')
                        x=date(today.year-i,m,1).weekday()
                        bufi=0 if(x==5 or x==6)else x
                    src=float(dc[k].replace(',',''))
                    dst=float(dc[l].replace(',',''))
                    buf[bufi]='+'if src<dst else'-'if src>dst else'='
                    bufi+=1
                    break
    print("")
