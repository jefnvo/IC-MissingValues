import pandas as pd
import numpy as np
from scipy.spatial import distance as dc
from sklearn.cluster import KMeans

dataset = pd.read_csv('dados.csv')
dados = dataset.iloc[:, [0,1,2,3]].values

# Aplicando k-means
kmeans = KMeans(n_clusters = 3, random_state  = 0)
y_kmeans = kmeans.fit_predict(dados)





#Indice Dunn

#    Este indice foi proposto por Dunn em 1974 e sua logica consiste em identificar cluster compactos e bem separados.
#    É definido da seguinte forma:
#        (1) deve-se calcular a minima distancia entre dois pontos de diferentes clusters.
#        (2) em seguida, deve-se calcular maxima distancia entre dois pontos dentre todos os cluters.
#        (3) deve-se divir o resultado de (1) por (2).
#        (4) busca-se o minimo valor de (3).
#    
#    
#    Este indice apresenta alto custo computacional se comparado a outros
#    e tambem é sensivel a ruidos nos dados, já que estes podem aumentar 
#    o valor do denominador ( diam(c) )
#    
#    Neste indice, todos os clusters sao comparados entre si.



#Separando cada cluster em uma lista, e inserindo-os em uma quarta lista, pra calcular as distancias euclidianas entre os pontos
c0=[]
c1=[]
c2=[]

indice = 0
for x in y_kmeans:
    if x == 0:
        c0.append(indice)
    elif x == 1:
        c1.append(indice)
    else:
        c2.append(indice)
    indice+=1
    
data=[]
data.append(c0)
data.append(c1)
data.append(c2)


#Buscando a minima distancia entre 2 pontos de 2 clusters diferentes
def d (c_i, c_j):
    min = dc.euclidean(dados[c_i[0]], dados[c_j[0]])
    
    for x in c_i:
        for y in c_j:
            aux = dc.euclidean(dados[x],dados[y])
            if aux < min:
                min = aux 
                
    return min

#Buscando a maxima distancia entre 2 pontos de 1 mesmo cluster
def diam (c_k):
    max = dc.euclidean(dados[c_k[0]], dados[c_k[1]])
    
    for x in c_k:
        for y in c_k:
            aux = dc.euclidean(dados[x],dados[y])
            if aux > max:
                max = aux 
    
    return max
    
#Buscando a maxima distancia entre 2 pontos dentre todos os clusters
def maxDiam (data,nC):
    max = diam(data[0])
    
    for x in range(0,nC):
        aux = diam(data[x])
        if aux > max:
            aux = max
            
    return max
            
         
def Dunn1 (data, i, nC):
    min = d(data[i], data[i+1])                #inicializando o minimo
    
    for j in range(i+1, nC):                   #variando j de i+1 ate 2
        aux = d(data[i], data[j])
        if aux < min:
            aux = min
        
    return (min/maxDiam(data, nC))


def Dunn2 (data, nC):
    min = Dunn1(data, 0, nC)                    #inicializando o minimo
    
    for i in range(0,nC):                       #começando com i em 0 ate 2
        aux = Dunn1(data, i, nC)    
        if aux < min:
            aux = min
            
    return min


resultado = Dunn2(data, 2)