
import csv

def motorstate():
    aa="MOTOR.csv"
    with open(aa,mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        return(data[0][0])

print(motorstate())