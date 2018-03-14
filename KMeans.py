import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from ssw_ssb import ssw, ssb
from calinski import calinski
from BH import ball_hall
from xu import xu_score
import copy

def KMeansInterface(path, sheet):
    db = pd.read_excel(path, sheetname=sheet)
    X = StandardScaler().fit_transform(db)
    #aplicando k-means
    kmeans = KMeans(n_clusters=3, init='k-means++',max_iter=300,n_init=10,random_state=0).fit(X)
    y_kmeans = kmeans.fit_predict(X)
    
    #armazenando os centroides separadamente
    centroides = kmeans.cluster_centers_
    labels = kmeans.labels_
    n_clusters_ = len(set(labels)) 
    c1 = c2 = c3 = 0
    for x in labels:
        if x == 0:
            c1 += 1
        elif x == 1:
            c2 += 1
        else:
            c3 += 1
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
    
    print("There are %d items in cluster 0" %c1)
    print("There are %d items in cluster 1" %c2)
    print("There are %d items in cluster 2" %c3)
    
    
    labels = copy.deepcopy(list(labels))
    print("SSW: \n",ssw(X,data,centroides, n_clusters_))
    print("SSB: \n",ssb(X,data,centroides))
    print("Calinski: \n", calinski(X,data,centroides, n_clusters_))
    print("Ball and Hall: \n", ball_hall(X,data,centroides,n_clusters_))
    print("Xu index \n", xu_score(X,data,centroides, n_clusters_))
    
