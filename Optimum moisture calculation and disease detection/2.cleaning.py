from datetime import datetime
from inspect import currentframe
import numpy as np
import matplotlib.pyplot as plt
import csv,time,os
from scipy.signal import find_peaks
from scipy.ndimage import gaussian_filter1d
import numpy as np
from scipy.signal import argrelmin, argrelmax
from scipy.interpolate import make_interp_spline
import time as time1
import cv2 as cv
import pandas as pd


def put1 (a):
    aa="CLEANDATA.csv"
    with open(aa,mode='a',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerows([a]) 
        csvfile.close()
        
        
        
data=[]
with open("MAINDATA.csv",mode='r') as csvfile :     #feeding each values to csv
    data=list(csv.reader(csvfile))
    csvfile.close()
    print(data)
temp=[]
moist=[]
hum=[]
xcr=[]
ycr=[]
n=[]
tt=[]
qindex=[]
u=0
for a in data:

    temp.append(int(a[0]))
    moist.append(int(a[1]))
    hum.append(int(a[2]))
    xcr.append(int(a[3]))
    ycr.append(int(a[4]))
    qindex.append(int(a[5]))
    #tt.append(float(a[6]))          #a=[temp,moist..........]

le=len(temp)
for d in range(0,le):
    n.append(d)


    
         
x1=[23,57,53,23,86,90,30,45]
y1=[3,7,3,3,6,0,10,5]

tempsmooth = gaussian_filter1d(temp,4)
humsmooth=gaussian_filter1d(moist,3)
moistsmooth=gaussian_filter1d(hum,3)



tmin=np.min(tempsmooth)
tmax=np.max(tempsmooth)
hmin=np.min(humsmooth)
hmax=np.max(humsmooth)
mmin=np.min(moistsmooth)
mmax=np.max(moistsmooth)
print("MIN TEMP",tmin)
print("MAX TEMP",tmax)
print("MIN HUM",hmin)
print("MAX HUM",hmax)
print("MIN MOIST",mmin)
print("MAX MOIST",mmax)

#smooth declared













#cleaning
xnew=[]
ynew=[]
znew=[]
nnew=[]
xcrnew=[]
ycrnew=[]
qindexnew=[]
#ttnew=[]

        
for i in range (0,le):
    if temp[i]>=tmin and temp[i]<=tmax and moist[i]>=hmin and moist[i]<=hmax and hum[i]>=mmin and hum[i]<=mmax:
        xnew.append(temp[i])
        ynew.append(moist[i])
        znew.append(hum[i])
        xcrnew.append(xcr[i])
        ycrnew.append(ycr[i])
        qindexnew.append(qindex[i])
        #ttnew.append(tt[i])
        nnew.append(i)



csvdata = []
for w in range(0,len(xnew)):
    csvdata.append([xnew[w],ynew[w],znew[w],xcrnew[w],ycrnew[w],qindexnew[w]])

df = pd.DataFrame(csvdata)
df.to_csv("CLEANDATA.csv", header=False, index=False)
print(df)

plt.clf()
plt.plot(n,temp)
plt.plot(n,moist)
plt.plot(n,hum)
#plt.plot(n,tempsmooth)
#plt.plot(n,humsmooth)
#plt.plot(n,moistsmooth)
plt.plot(nnew,xnew)
plt.plot(nnew,ynew)
plt.plot(nnew,znew)
#plt.draw()
os.remove('MAINDATA.csv')
plt.pause(10)
plt.clf()




    