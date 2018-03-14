# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 13:59:05 2017

@author: Vinicius
"""


import math as ma
from ssw_ssb import ssw

def xu_score (dataset, labels, centroids, nC):
    d = dataset.shape[1]
    n = dataset.shape[0]

    
    num = ssw(dataset, labels, centroids, nC)
    den = d*(n**2)
    
    aux = ma.sqrt(num/den)
    
    aux2 = d*ma.log2(aux)
    
    return (aux2 + ma.log10(nC))