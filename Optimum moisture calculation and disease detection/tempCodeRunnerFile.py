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
                
                CURRENTCSVSPLITTER.do()
    