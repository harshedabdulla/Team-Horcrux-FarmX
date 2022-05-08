import csv


def do():
    data1=[]
    with open("CURRENT.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        csvfile.close()


    def put1 (a):
        aa="PLANT"+str(a[3])+str(a[4])+".csv"
        with open(aa,mode='w',newline="") as csvfile :     #feeding each values to csv
            mywriter=csv.writer(csvfile)
            mywriter.writerows([a]) 
            csvfile.close()
        print("done")


    x=3
    y=3
    for a in data:
        for c in range (0,x+1):
            for b in range (0,y+1):
                if a[3]==c and a[4]==b:
                    put1(a)
            #print(data1)
        #print(" ")