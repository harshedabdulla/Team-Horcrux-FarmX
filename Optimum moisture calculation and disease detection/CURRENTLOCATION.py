import csv
import random as r
import time
import CURRENTCSVSPLITTER,motorread

def qread():
    with open("QINDEX.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        row=len(data) 
        a=data[row-2][0]
        
        print(row)
        csvfile.close()
        print("done")
        return a


def put1 (temp,hum,moist,crx,cry,qindex,motorstate):
    with open("CURRENT.csv",mode='a',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerow([temp,hum,moist,crx,cry,qindex,motorstate]) 
        csvfile.close()
        print("done")


x=1
y=1

def runthis(delay):

    while(1):
        
        con=0
        with open("condition.csv",mode='r') as csvfile:
            data=list(csv.reader(csvfile))
            con1=int(data[0][0])
            con=con1
            
        if con==0:
            for a in range (1,4):
                for b in range (1,4):
                    temp=r.randint(26,29)
                    hum=r.randint(76,79)
                    moist=r.randint(80,90)
                    qindex=qread()
                    
                    crx=a
                    cry=b
                    motorstate=motorread.motorstate()
                    put1(temp,moist,hum,crx,cry,qindex,motorstate)
                    time.sleep(delay)
                    CURRENTCSVSPLITTER.do()
    

                
runthis(0.5)