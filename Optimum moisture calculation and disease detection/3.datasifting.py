import pandas as pd



df = pd.read_csv("CLEANDATA.csv", header=None)
#print(df.head())


#print(df[df[3]==1])
for i in range(1,6):
	for j in range(1,6):
		filename = "PLANT"+ str(i)+str(j) + ".csv"
		desired = df[df[3]==i][df[4]==j]
		desired.to_csv(filename, header=False, index=False)
		#print(desired.head())
