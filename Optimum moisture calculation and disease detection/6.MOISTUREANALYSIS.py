from datetime import datetime
from enum import unique
from inspect import currentframe
import numpy as np
import matplotlib.pyplot as plt
import csv,time,os
from scipy.ndimage import gaussian_filter1d
import numpy as np
import time as time1
import cv2 as cv
from sympy import true
import TELLHOMEPAGE


plt.figure()
while True:

    datax=[]
    with open("CURRENT.csv",mode='r') as csvfile :     #feeding each values to csv
        datax=list(csv.reader(csvfile))
        csvfile.close()
    #print(datax)
    xcoor=int(datax[len(datax)-1][3])
    ycoor=int(datax[len(datax)-1][4])

    data=[]
    with open("PLANT"+str(xcoor)+str(ycoor)+".csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        csvfile.close()
        
        
    x=[]
    y=[]
    z=[]
    t=[]
    p=0
    #con=float(data[0][6])
    for a in data:
        p=p+1
        if p<40000:
            x.append(int(a[0])) #temp only list
            y.append(int(a[1])) #moist only list
            z.append(int(a[2])) #hum only list
            #t.append(float(a[6]))  #time only list
            

    tmin=np.min(x)
    tmax=np.max(x)
    hmin=np.min(y)
    hmax=np.max(y)
    f=0
    val=[]
    val1=[]
    for som in range(tmin,tmax):


        for o in range(0,len(x)):
            if som==x[o]:
                val1.append(o)
        print("newwwwwwwwwww")
        #print(val1)
        val1=[]
        val.append(val1)
    print("          -")
    #print("finalllllllllllllllllllll temp indexs:",val)
    print("          -")
    print("          -")
    print("          -")

    val22=[]
    val2=[]
    for j in range(0,len(val)):
        for k in range(0,len(val[j])):
            val2.append(int(data[val[j][k]][2]))
        val22.append(val2)
        val2=[]

    #print(val22)

    uni=[]
    unit=[]
    unih=[]
    uni1=[]
    uniT=[]
    uniH=[]
    uniM=[]
    uniS=[]
    unim=[]
    unis=[]
    for som1 in range(0,len(val)):
        if len(val[som1])!=0:
            for aa in range (min(val22[som1]),max(val22[som1])):
                for bb in range (0,len(val[som1])):
                    if aa==val22[som1][bb]:
                        uni1.append(int(val[som1][bb]))
                        unit.append(int(data[val[som1][bb]][0]))
                        unih.append(int(data[val[som1][bb]][2]))
                        unim.append(int(data[val[som1][bb]][1]))
                        #unis.append(float(data[val[som1][bb]][6]))
                uni.append(uni1)
                uniT.append(unit)
                uniH.append(unih)
                uniM.append(unim)
                #uniS.append(unis)
                uni1=[]
                unit=[]
                unih=[]
                unis=[]
                unim=[]


    #print(uniS)
    #for humidi in range(hmin,hmax):
        #for hh in range(0,len(val[humidi-hmin])):
            #for ll in range()
            #if humidi==val[hh]
    datax=[]
    with open("CURRENT.csv",mode='r') as csvfile :     #feeding each values to csv
        datax=list(csv.reader(csvfile))
        csvfile.close()
    #print(datax)
    xtemp=int(datax[len(datax)-1][0])
    xhum=int(datax[len(datax)-1][2])

    print("xtemp:",xtemp)
    print("xhum:",xhum)
    #data[val[som1][bb]][0] 
    #data[val[som1][bb]][2]
    #xplot=[]
    #for p in range(0,len(val)):
        #for d in range(0,len(val[p])):
            #if xtemp==data[ val[p][d] ] [0] and xhum==data[ val[p][d] ][2]:
                #xplot.append(data[ val[d][p] ][1])


    xx=[]
    for y in range(0,len(uniT)):
        if len(uniT[y])!=0:
            if xtemp==int(uniT[y][0]):
                xx.append(y)

    yy=[]
    for y in range(0,len(uniH)):
        if len(uniH[y])!=0:
            if xhum==int(uniH[y][0]):
                yy.append(y)
    #print(xx)
    #print(yy)


    xx_set=set(xx)
    yy_set=set(yy)
    ccc=0
    if(xx_set & yy_set):
        cc=xx_set & yy_set
        cc1=list(cc)
        ccc=cc1[0]
        print(ccc)
        
    else:
        
        
        
        
        
        #prediction
        
        vhum=[]
        for d in range(0,len(uniH)):
            vhum.append(int(uniH[d][0]))
        unique_hum=[]
        for s in vhum:
            if s not in unique_hum:
                unique_hum.append(s)
        #print("vtemp:",vhum)
        #print("uni hum",unique_hum)    
            
        vtemp=[]
        for d in range(0,len(uniT)):
            vtemp.append(int(uniT[d][0]))

        #print("vtemp:",vtemp)

        unique_temp=[]
        for v in vtemp:
            if v not in unique_temp:
                unique_temp.append(v)
        #print("uni temp",unique_temp)
        
        
        if xtemp not in unique_temp:   
            
                    
            #case upper* lower-ok
            
            
            vhum=[]
            for d in range(0,len(uniH)):
                vhum.append(int(uniH[d][0]))
            unique_hum=[]
            for s in vhum:
                if s not in unique_hum:
                    unique_hum.append(s)
            #print("vtemp:",vhum)
            #print("uni hum",unique_hum)    
                
            vtemp=[]
            for d in range(0,len(uniT)):
                vtemp.append(int(uniT[d][0]))
            
            #print("vtemp:",vtemp)
            
            unique_temp=[]
            for v in vtemp:
                if v not in unique_temp:
                    unique_temp.append(v)
            #print("uni temp",unique_temp)
            
            add_hum=[]           
            if xhum in unique_hum:
                for deu in range(0,len(uniH)):
                    if xhum==uniH[deu][0]:
                        add_hum.append(deu)
                        
            #print("address:",add_hum)
            
            aa_add_le_temp=[]
            for heu in range(0,len(add_hum)):
                aa_add_le_temp.append(uniT[add_hum[heu]][0])
                
            #print("adress temp:",aa_add_le_temp)
            
            
            aa_add_le_moist=[]
            for heu in range(0,len(add_hum)):
                aa_add_le_moist.append(uniM[add_hum[heu]][0])
                
            #print("adress moist:",aa_add_le_moist)
            
            aa_add_le_hum=[]
            for heu in range(0,len(add_hum)):
                aa_add_le_hum.append(uniH[add_hum[heu]][0])
                
            #print("adress hum:",aa_add_le_hum)
                
            
                    
            if xtemp>aa_add_le_temp[len(aa_add_le_temp)-1]:
                C=0  
                nnn=xtemp-aa_add_le_temp[len(aa_add_le_temp)-1]-1
                for que in range(0,len(aa_add_le_moist)-1):
                    C=aa_add_le_moist[que+1]-aa_add_le_moist[que]+C
                    
                meanC=C/(len(aa_add_le_moist)-1)
                
                predictedtemp=aa_add_le_moist[len(aa_add_le_moist)-1]+(nnn*meanC)

                print("predcited moisture:",predictedtemp)
                    
            
            #case upper-ok lower*
            if xtemp<aa_add_le_temp[0]:
                C=0  
                nnn=aa_add_le_temp[0]-1-xtemp
                for que in range(0,len(aa_add_le_moist)-1):
                    C=-aa_add_le_moist[que+1]+aa_add_le_moist[que]+C
                    
                meanC=C/(len(aa_add_le_moist)-1)
                
                predictedtemp=aa_add_le_moist[0]+(nnn*meanC)

                print("predicted moisture:",predictedtemp)
                
                
                
                
        
        if xhum not in unique_hum:            
            #case upper* lower-ok
            
            
            vtemp=[]
            for d in range(0,len(uniT)):
                vtemp.append(int(uniT[d][0]))
            unique_temp=[]
            for s in vtemp:
                if s not in unique_temp:
                    unique_temp.append(s)
            print("vtemp:",vtemp)
            print("uni temp",unique_temp)    
                
            vhum=[]
            for d in range(0,len(uniH)):
                vhum.append(int(uniH[d][0]))
            
            print("vhum:",vhum)
            
            unique_hum=[]
            for v in vhum:
                if v not in unique_hum:
                    unique_hum.append(v)
            #print("uni hum",unique_hum)
            
            add_temp=[]           
            if xtemp in unique_temp:
                for deu in range(0,len(uniT)):
                    if xtemp==uniT[deu][0]:
                        add_temp.append(deu)
                        
            #print("address:",add_temp)
            
            aa_add_le_hum=[]
            for heu in range(0,len(add_temp)):
                aa_add_le_hum.append(uniH[add_temp[heu]][0])
                
            #print("adress hum:",aa_add_le_hum)
            
            
            aa_add_le_moist=[]
            for heu in range(0,len(add_temp)):
                aa_add_le_moist.append(uniM[add_temp[heu]][0])
                
            #print("adress moist:",aa_add_le_moist)
            
            aa_add_le_temp=[]
            for heu in range(0,len(add_temp)):
                aa_add_le_temp.append(uniT[add_temp[heu]][0])
                
            #print("adress temp:",aa_add_le_temp)
            
                    
            if xhum>aa_add_le_hum[len(aa_add_le_hum)-1]:
                C=0  
                nnn=xhum-aa_add_le_hum[len(aa_add_le_hum)-1]-1
                for que in range(0,len(aa_add_le_moist)-1):
                    C=aa_add_le_moist[que+1]-aa_add_le_moist[que]+C
                    
                meanC=C/(len(aa_add_le_moist)-1)
                
                predictedhum=aa_add_le_moist[len(aa_add_le_moist)-1]+(nnn*meanC)

                print("predcited moisture:",predictedhum)
                    
            
            #case upper-ok lower*
            if xhum<aa_add_le_hum[0]:
                C=0  
                nnn=aa_add_le_hum[0]-1-xhum
                for fue in range(0,len(aa_add_le_moist)-1):
                    C=-aa_add_le_moist[fue+1]+aa_add_le_moist[fue]+C
                    
                meanC=C/(len(aa_add_le_moist)-1)
                
                predictedhum=aa_add_le_moist[0]+(nnn*meanC)

                print("predicted moisture:",predictedhum)

        
        
        
    yplot=uniM[ccc]
    xplot=[]
    for u in range(0,len(yplot)):
        xplot.append(u)



    #print(yplot)
    #print(xplot)
    curve = gaussian_filter1d(yplot, 2)
    #print(curve)
    #plt.plot(xplot,yplot)
    #plt.plot(curve)
    #plt.draw()


    week=[]
    lenx=len(curve)
    for f in range(int(lenx-(lenx*(7/30))),lenx):
        week.append(curve[f])

    #print(week)

    weekcurve=gaussian_filter1d(week,10)

    figure , axis = plt.subplots(2,2)
    axis[0,0].plot(week)
    axis[0,0].plot(weekcurve)
    axis[0,0].set_title("weakly optimum moisture")

    axis[0,1].plot(xplot,yplot)
    axis[0,1].plot(curve)
    axis[0,1].set_title("total optimum moisture")


    

    plt.pause(1)
    plt.close()

    cord=[]
    
    cord.append(week)
    cord.append(weekcurve)
    cord.append(yplot)
    cord.append(xplot)
    cord.append(curve)
        
    file= open("Cordinates.csv",mode='a',newline='')   
    with file:    
        write=csv.writer(file)
        write.writerows(cord)
        file.close()

    #decide motor on or off
    hhh=TELLHOMEPAGE.crmoist()
    print("OPTIMUM MOIST",weekcurve[len(weekcurve)-1])
    print("CURRENT MOIST",hhh) 
    
   
    if weekcurve[len(weekcurve)-1]>hhh:
        f=open('MOTOR.csv', mode='w')
        writer=csv.writer(f)
        value=1
        writer.writerow([value])
        f.close()
        print("on")

        
    
    if weekcurve[len(weekcurve)-1]<hhh:
        f=open('MOTOR.csv', mode='w')
        writer=csv.writer(f)
        value=0
        writer.writerow([value])
        f.close()
        print("off")

