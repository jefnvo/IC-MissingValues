import pandas as pd
import numpy as np

#lendo dataset
dataset = pd.read_csv('dados.csv')
X = dataset.iloc[:,[0,1,2,3]].values
G = dataset.iloc[:,[4]].values
g1=[]
g2=[]
g3=[]
gt=[]

for x in G:
    if x == 'Iris-setosa':
        g1.append(0)
    elif x == 'Iris-versicolor':
        g2.append(1)
    else:
        g3.append(2)

gt.append(g1)
gt.append(g2)
gt.append(g3)
centroide1 = np.mean(X[0:48,[0,1,2,3]], axis= 0)
centroide2 = np.mean(X[49:98,[0,1,2,3]], axis= 0)
centroide3 = np.mean(X[99:148,[0,1,2,3]], axis= 0)
cgt = [[centroide1], [centroide2],[centroide3]]

