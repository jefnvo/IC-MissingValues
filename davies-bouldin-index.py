import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as mt
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from scipy.spatial import distance

def dispersion_s(n_elements, labels, dataset, centroid):
    somatorio = 0
    for x in labels:
        somatorio+=distance.euclidean(dataset[x,:], centroid)
    
    dispersion = (1/n_elements)*somatorio    
    return dispersion

def Rij(si, sj, centroids, labels, dataset):
    distance_euclidean = distance.euclidean(centroids[si],centroids[sj])
    calc = (dispersion_s(len(labels[si]), labels[si], dataset, centroids[si])+
            dispersion_s(len(labels[sj]), labels[sj], dataset, centroids[sj]))
    calc = calc / distance_euclidean
    return calc

def maxRi(i, dataset, centroids, nc, labels):
    maximo = Rij(0,1, centroids, labels, dataset)
    aux = 0
    for i in range(nc):
        for j in range(nc):
            if i!=j:
                if i<j:
                    aux = Rij(i,j,centroids,labels, dataset)
                    if aux > maximo:
                        maximo = aux
    return maximo
                        
def DB(nc, dataset, centroids, labels):
    sigma=0
    for i in range(nc):
        sigma+=maxRi(i, dataset, centroids, nc, labels)
    db_index= sigma/nc
    return db_index

dataset = pd.read_csv('dados.csv')
X = dataset.iloc[:,[0,1,2,3]].values
#aplicando o K-means
kmeans = KMeans(n_clusters = 3, init = 'k-means++',max_iter = 300, n_init = 10, 
                random_state = 0)
y_kmeans = kmeans.fit_predict(X)

#achando os centroids
centroids = kmeans.cluster_centers_
#calculando distancias
#min_dist = np.min(cdist(X, centroids, 'euclidean'), axis=0)
#Separando os 3 clusters em 3 listas, e inserindo-os em uma quarta lista, pra calcular as distancias euclidianas entre os pontos
v1=[]
v2=[]
v3=[]
    
indice = 0
for x in y_kmeans:
    if x == 0:
        v1.append(indice)
    elif x == 1:
        v2.append(indice)
    else:
        v3.append(indice)
    indice+=1
    
data=[]
data.append(v1)
data.append(v2)
data.append(v3)
result = DB(3, X, centroids, data)
print("The DB_index is:", result)














def ssb(dataset, labels, centroids):
    n = len(dataset)
    result = 0
    media=[]
    media=dataset.mean(1)
    media2=0
    for x in range(len(media)):
        media2+=
    for i in range(len(data)):
        result += len(data[i])*LA.norm(centroids[i] - )

    
