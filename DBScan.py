from sklearn.neighbors import NearestNeighbors
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

def DBScanInterface(path, sheet):
    db = pd.read_excel(path, sheetname=sheet)
    X = StandardScaler().fit_transform(db)
    
    nbrs = NearestNeighbors(n_neighbors=45).fit(X)
    distances, indices = nbrs.kneighbors(X)
    
    
    # Compute DBSCAN
    db = DBSCAN(eps = 2.3, min_samples = 13).fit(X)
    
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    print("Silhouette Coefficient: %0.3f"
          % metrics.silhouette_score(X, labels))
    print('Estimated number of clusters: %d' % n_clusters_)
    # #############################################################################
    # Plot result
    import matplotlib.pyplot as plt
    
    # Black removed and is used for noise instead.
    unique_labels = set(labels)
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0, 1, len(unique_labels))]
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]
    
        class_member_mask = (labels == k)
    
        xy = X[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=14)
    
        xy = X[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=6)
    
    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()
    c1 = c2 = c3 = 0
    
    for x in labels:
        if x == 0:
            c1 += 1
        elif x == 1:
            c2 += 1
        else:
            c3 += 1
    
    print("There are %d items in cluster 0" %c1)
    print("There are %d items in cluster 1" %c2)
    print("There are %d items in cluster 2" %c3)
