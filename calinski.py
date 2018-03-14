# -- coding: utf-8 --
"""
Created on Sun Jun 18 23:47:24 2017

@author: Vinicius
"""

"""
    O indice Calinski and Harabasz foi publicado em 1972 é
    baseado nos valores obtidos a partir das somas ssw e
    ssb. O resultado é obtido através da razão entre a dispersão 
    interna de cada cluster e a dispersão externa entre os clusters
"""

"""
    Os parametros recebidos nesta implementação são:
        labels = lista de listas separando cada cluster que contêm os indices usados no dataset
        dataset = matriz contendo os dados. Cada linha representa um ponto.
        *nC = numero de clusters
        *centroids = lista contendo as coordenadas de cada centroide gerado pelo algoritmo
"""


from ssw_ssb import ssw, ssb

def calinski (dataset, labels, centroids, nC):
    
    numerator = ssb(dataset, labels, centroids)
    numerator = numerator/(nC-1)
    
    denominator = ssw(dataset, labels, centroids, nC)
    denominator = denominator/(len(dataset)-nC)
    
    return (numerator/denominator)