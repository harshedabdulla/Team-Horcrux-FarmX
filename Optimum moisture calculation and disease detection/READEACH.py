import csv
def moist(a):
    if a==1:
        a=11
    if a==2:
        a=12
    if a==3:
        a=13
    if a==4:
        a=21
    if a==5:
        a=22
    if a==6:
        a=23
    if a==7:
        a=31
    if a==8:
        a=32
    if a==9:
        a=33
    aa="READSPLIT"+str(a)+".csv"
    with open(aa,mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        return(data[0][2])
        
def color(a):
    a=int(a)
    if a==1:
        a=11
    if a==2:
        a=12
    if a==3:
        a=13
    if a==4:
        a=21
    if a==5:
        a=22
    if a==6:
        a=23
    if a==7:
        a=31
    if a==8:
        a=32
    if a==9:
        a=33


    aa="READSPLIT"+str(a)+".csv"
    with open(aa,mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))

        if int(data[0][5])==6:
            data[0][5]=1   #red
            return(data[0][5])
        if int(data[0][5])>=4:
            data[0][5]=2  #green
            return(data[0][5])
        if  int(data[0][5])<4:
            data[0][5]=3 #orange
            return(data[0][5])
        


def motor(a):
    if a==1:
        a=11
    if a==2:
        a=12
    if a==3:
        a=13
    if a==4:
        a=21
    if a==5:
        a=22
    if a==6:
        a=23
    if a==7:
        a=31
    if a==8:
        a=32
    if a==9:
        a=33
    aa="READSPLIT"+str(a)+".csv"
    with open(aa,mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        return(data[0][6])

def humidity(a):
    if a==1:
        a=11
    if a==2:
        a=12
    if a==3:
        a=13
    if a==4:
        a=21
    if a==5:
        a=22
    if a==6:
        a=23
    if a==7:
        a=31
    if a==8:
        a=32
    if a==9:
        a=33
    aa="READSPLIT"+str(a)+".csv"
    with open(aa,mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        return(data[0][1])


def temp(a):
    if a==1:
        a=11
    if a==2:
        a=12
    if a==3:
        a=13
    if a==4:
        a=21
    if a==5:
        a=22
    if a==6:
        a=23
    if a==7:
        a=31
    if a==8:
        a=32
    if a==9:
        a=33
    aa="READSPLIT"+str(a)+".csv"
    with open(aa,mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        return(data[0][0])