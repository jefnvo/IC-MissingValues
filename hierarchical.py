import numpy as np
import time as time
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler 

def HierarchicalInterface(path, sheet):
    db = pd.read_excel('Datasets/wine.xlsx', sheetname=0)
    X = StandardScaler().fit_transform(db)
    # Compute clustering
    print("Compute structured hierarchical clustering...")
    st = time.time()
    
    n_clusters = 3  # number of regions
    ward = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
    ward.fit(X)
    label = ward.labels_
    print("Elapsed time: ", time.time() - st)
    print("Number of pixels: ", label.size)
    print("Number of clusters: ", np.unique(label).size)
    
    # #############################################################################
    
    plt.scatter(X[:,0], X[:,1])
    plt.show()
    
    n_clusters_ = len(set(label)) 
    c1 = c2 = c3 = 0
    for x in label:
        if x == 0:
            c1 += 1
        elif x == 1:
            c2 += 1
        else:
            c3 += 1
    
    print("There are %d items in cluster 0" %c1)
    print("There are %d items in cluster 1" %c2)
    print("There are %d items in cluster 2" %c3)
