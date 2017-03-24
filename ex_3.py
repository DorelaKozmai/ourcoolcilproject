import numpy as np 
import csv

coordinates = []  
ratings = []      

with open('data_train.csv','r') as fin:
    reader=csv.reader(fin,delimiter=',')
    for row in reader:
  		coordinates.append(row[0])
		ratings.append(row[1])

Xs=[]
Ys=[]
for coordinate in coordinates:
	X, de, Y = coordinate.partition('_')
	X = X[1:]
	Y = Y[1:]	
	Xs.append(X)
	Ys.append(Y)

Xs = Xs[1:]
Ys = Ys[1:]

Xs = [int(x) for x in Xs]
Ys = [int(y) for y in Ys]

XS = np.array(Xs)
YS = np.array(Ys)


XS = XS-1
YS = YS-1

np.zeros((10000,1000))

