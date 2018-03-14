from ssw_ssb import ssw
'''
The Ball-Hall index is the mean, through all the clusters, of their mean dispersion
'''
def ball_hall(dataset,labels,centroid,nc):
    index = (ssw(dataset,labels, centroid, nc))/nc
    return index

    