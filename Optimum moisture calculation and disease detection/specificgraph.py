import csv

data=[]
with open("SPLIT11.csv",mode='r') as csvfile :     #feeding each values to csv
    data=list(csv.reader(csvfile))
    csvfile.close()
    
x=[]
y=[]
z=[]
t=[]

for a in data:

    x.append(int(a[0]))
    y.append(int(a[1]))
    z.append(int(a[2]))
    t.append(float(a[6]))
        
        
print(t)