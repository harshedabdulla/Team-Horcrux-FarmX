import csv



def curvelast():
    data=[]
    with open("Cordinates.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        csvfile.close()
      
    lstcurve=[]
    lendt=len(data)
    for i in data[lendt-1]:
        lstcurve.append(int(i))
    return i
    
    
curv=[]
def curve():
    data=[]
    with open("Cordinates.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        csvfile.close()
       
  
    for u in data[len(data)-1]:
        curv.append(int(u))
    return(curv)
 
xplo=[]    
def xplot():
    data=[]
    with open("Cordinates.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        csvfile.close()
        
  
    for u in data[len(data)-2]:
        xplo.append(int(u))
    return(xplo)
    
yplo=[]        
def yplot():
    data=[]
    with open("Cordinates.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        csvfile.close()
   
    
    for u in data[len(data)-3]:
        yplo.append(int(u))
    return(yplo)


wkcurve=[]        
def weekcurve():
    data=[]
    with open("Cordinates.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        csvfile.close()
     
    for u in data[len(data)-4]:
        wkcurve.append(int(u))
    return(wkcurve)

wee=[]
def week():
    data=[]
    with open("Cordinates.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        csvfile.close()
      
    for u in data[len(data)-5]:
        wee.append(int(u))
    return(wee)





