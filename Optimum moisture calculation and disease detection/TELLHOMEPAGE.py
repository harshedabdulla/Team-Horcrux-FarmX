import csv



def crtemp():


    
    data2=[]
    with open("CURRENT.csv",mode='r',) as csvfile :     #feeding each values to csv
        data2=list(csv.reader(csvfile))
        csvfile.close()
    lentt=len(data2)-1
    u=int(data2[lentt][0])
    return u

def crmoist():
    data2=[]
    with open("CURRENT.csv",mode='r') as csvfile :     #feeding each values to csv
        data2=list(csv.reader(csvfile))
        csvfile.close()

    
    data2=[]
    with open("CURRENT.csv",mode='r',) as csvfile :     #feeding each values to csv
        data2=list(csv.reader(csvfile))
        csvfile.close()
    lentt=len(data2)-1
    u=int(data2[lentt][1])
    return u

def crhum():
    data2=[]
    with open("CURRENT.csv",mode='r') as csvfile :     #feeding each values to csv
        data2=list(csv.reader(csvfile))
        csvfile.close()

    
    data2=[]
    with open("CURRENT.csv",mode='r',) as csvfile :     #feeding each values to csv
        data2=list(csv.reader(csvfile))
        csvfile.close()
    lentt=len(data2)-1
    u=int(data2[lentt][2])
    return u

def crx():
    data2=[]
    with open("CURRENT.csv",mode='r') as csvfile :     #feeding each values to csv
        data2=list(csv.reader(csvfile))
        csvfile.close()

    
    data2=[]
    with open("CURRENT.csv",mode='r',) as csvfile :     #feeding each values to csv
        data2=list(csv.reader(csvfile))
        csvfile.close()
    lentt=len(data2)-1
    u=int(data2[lentt][3])
    return u

def cry():
    data2=[]
    with open("CURRENT.csv",mode='r') as csvfile :     #feeding each values to csv
        data2=list(csv.reader(csvfile))
        csvfile.close()

    
    data2=[]
    with open("CURRENT.csv",mode='r',) as csvfile :     #feeding each values to csv
        data2=list(csv.reader(csvfile))
        csvfile.close()
    lentt=len(data2)-1
    u=int(data2[lentt][4])
    return u

def crindex():
    data2=[]
    with open("CURRENT.csv",mode='r') as csvfile :     #feeding each values to csv
        data2=list(csv.reader(csvfile))
        csvfile.close()

    
    data2=[]
    with open("CURRENT.csv",mode='r',) as csvfile :     #feeding each values to csv
        data2=list(csv.reader(csvfile))
        csvfile.close()
    lentt=len(data2)-1
    u=int(data2[lentt][5])
    return u

def crmotor():
    data2=[]
    with open("CURRENT.csv",mode='r') as csvfile :     #feeding each values to csv
        data2=list(csv.reader(csvfile))
        csvfile.close()


    data2=[]
    with open("CURRENT.csv",mode='r',) as csvfile :     #feeding each values to csv
        data2=list(csv.reader(csvfile))
        csvfile.close()
    lentt=len(data2)-1
    u=int(data2[lentt][6])
    return u