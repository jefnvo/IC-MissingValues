import pandas as pd
from numpy import linalg as LA
from sklearn.cluster import KMeans


'''
    calculando o somatorio interno
    dataset = conjunto de dados
    cluster = indices do elementos em um dado cluster
    centroid =  coordenadas dos centroides
'''

def sswInternal(dataset, cluster, centroid):
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
    somatorio = 0
    for x in range(nc):
       somatorio += sswInternal(dataset, labels[x], centroid)
       somatorio=somatorio/len(dataset)
    return somatorio

def ssb(dataset, labels, centroids):
    n = len(dataset) #pega o numero de observacoes no dataset
    result = 0
    media = sum(dataset.mean(1)) #pega a media dos elementos do dataset
    for i in range(len(data)):
        result += len(data[i])*LA.norm(centroids[i] - media)
    return result/n    

#############################################################################################

#lendo dataset
dataset = pd.read_csv('dados.csv')
#removendo a ultima coluna dos dados
X = dataset.iloc[:,[0,1,2,3]].values
Y = (datasets.load_iris()).target
#aplicando k-means
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300,n_init=10,random_state=0)
y_kmeans = kmeans.fit_predict(X)
#armazenando os centroides separadamente
centroides = kmeans.cluster_centers_
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
target_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
print("O indice SSW eh: ", ssw(X, data, centroides, 3))
print("\nO indice SSB eh: ", ssb(X, data, centroides))
