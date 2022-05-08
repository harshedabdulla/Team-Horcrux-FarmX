from email import header
import pandas as pd
import csv
import random as r
import time,datetime
import mysql.connector as sq 
import sqlite3

count=1000000  #hundred codes
X=5       #no of row of plant
Y=5       #no of col of plant

def put1 (a):
    aa="MAINDATA.csv"
    with open(aa,mode='a',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerow(a) 
        csvfile.close()
    print("done")


    
temp=0
hum=0
moist=0
xcr=0
ycr=0
qindex=0
sec=0.0
DATA=[]
for a in range (0,count):
    vv=r.randint(1,100000)
    if vv==5000:
        temp=r.randint(50,80)
    elif vv==21:
        temp=r.randint(0,10)

    elif vv==100:
        hum=r.randint(40,50)
    elif vv==50:
        hum=r.randint(90,100)

    elif vv==25:
        moist=r.randint(30,60)
    elif vv==78:
        moist=r.randint(92,98)
    
    else:
        temp=r.randint(25,30)
        moist=r.randint(80,90)
        hum=r.randint(75,80)
    
    xcr=r.randint(1,X)
    ycr=r.randint(1,Y)
    qindex=r.randint(1,5)
    #ttime=datetime.datetime.now()
    #sec=ttime.timestamp()
    

    #print(sec)
    data=[temp,moist,hum,xcr,ycr,qindex]
    DATA.append(data)

#print(DATA)
df=pd.DataFrame(DATA)
print(df)
df.to_csv("MAINDATA.csv",header=False,index=False)
#for w in range(0,len(DATA)):
 #   put1(DATA[w])

