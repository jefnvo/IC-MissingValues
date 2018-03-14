import copy
from numpy import linalg as LA

'''
    calculando o somatorio interno
    dataset = conjunto de dados
    cluster = indices do elementos em um dado cluster
    centroid =  coordenadas dos centroides
'''

def sswInternal(dataset, cluster, centroid):
    cluster = copy.deepcopy(list(cluster))
    somatorio = 0
    for i in cluster:
        somatorio+=LA.norm((dataset[i,:] - centroid))
    return somatorio
    
'''
    Calculando o somatorio externo
    
    dataset = conjunto de dados
    labels = sao os indices dos meus agrupamentos
    centroid = coordenadas dos centroids dos agrupamentos
    n = numero de clusters
'''

def ssw(dataset, labels, centroid, nc):
    labels = copy.deepcopy(list(labels))
    somatorio = 0
    for x in range(nc):
       somatorio += sswInternal(dataset, labels[x], centroid)
       somatorio=somatorio/len(dataset)
    return somatorio

def ssb(dataset, labels, centroids):
    n = len(dataset) #pega o numero de observacoes no dataset
    result = 0
    media = sum(dataset.mean(1)) #pega a media dos elementos do dataset
    for i in range(len(labels)):
        result += len(labels[i])*LA.norm(centroids[i] - media)
    return result/n