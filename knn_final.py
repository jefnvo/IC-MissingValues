import numpy as np
import pandas as pd
from statistical import imputationMean
from scipy.spatial.distance import cdist
import copy

#
#def distance_matrix(data, numeric_distance):#por hora nesse projeto ignoraremos distancias categoricas
#    #number_of_variables = data.shape[1]#colunas
#    #number_of_observations = data.shape[0]#tuplas  
#    
#    # Substitui os valores ausentes com a media da coluna
#    data = imputationMean(data)
#    
#    result_matrix = cdist(data, data, metric=numeric_distance)
#    # NaN para a diagonal
#    np.fill_diagonal(result_matrix, np.nan)
#    result_matrix = pd.DataFrame(result_matrix)
#    return result_matrix
#
#
#def knn_impute(target, attributes, k_neighbors, aggregation_method):
#    
#    # Get the distance matrix and check whether no error was triggered when computing it 
#    distances = distance_matrix(attributes, "euclidean")
#    #print("oi calculei as distancias necessarias")
#
#    if distances is None:
#        return None
#     #Make sure the data are in the right format
#    target = pd.DataFrame(target)
#    attributes = pd.DataFrame(attributes)
#
#            
#    # Get the closest points and compute the correct aggregation method
#    for i, value in enumerate(target.iloc[:, 0]):
#        if pd.isnull(value):
#            print("entra ?")
#            order = distances.iloc[i,:].values.argsort()[:k_neighbors]
#            closest_to_target = target.iloc[order, :]
#            target.iloc[i] = np.ma.mean(np.ma.masked_array(closest_to_target,np.isnan(closest_to_target)))
#            print("alo")
#            
#    column = target.values.tolist()
#    lista = []
#    for i in range(len(column)):
#        lista.append(column[i][0])
#    return lista


def distance_matrix(data, numeric_distance):#por hora nesse projeto ignoraremos distancias categoricas
    #number_of_variables = data.shape[1]#colunas
    #number_of_observations = data.shape[0]#tuplas  
    
    # Substitui os valores ausentes com a media da coluna
    result_matrix = imputationMean(data)
    
    result_matrix = cdist(result_matrix, result_matrix, metric=numeric_distance)
    #NaN para a diagonal
    np.fill_diagonal(result_matrix, np.nan)
    result_matrix = pd.DataFrame(result_matrix)
    return result_matrix


def knn_impute(target, attributes, k_neighbors, aggregation_method):
    tupla = copy.deepcopy(target)
    dados = copy.deepcopy(attributes)
    #print("O q ocorre? \n",tupla)
    
    # Get the distance matrix and check whether no error was triggered when computing it 
   
    distances = distance_matrix(dados, "euclidean")
    #print("oi calculei as distancias necessarias")
    if distances is None:
        return None
     #Make sure the data are in the right format
    tupla = pd.DataFrame(tupla)
    dados = pd.DataFrame(dados)

            
    # Get the closest points and compute the correct aggregation method
    for i, value in enumerate(tupla.iloc[:, 0]):
        if value == "MISSING":
            #pega os k primeiros indices ordenados
            order = distances.iloc[i,:].values.argsort()[:k_neighbors]
            closest_to_target = dados.iloc[order, :]

            tupla.iloc[i] = tupla.iloc[i].replace("MISSING", np.NaN)
            tupla.iloc[i] = np.ma.mean(np.ma.masked_array(closest_to_target,np.isnan(closest_to_target)))
            mean = 0
            for item in closest_to_target[i]:
                mean = mean + item
            mean = mean /3
            tupla.iloc[i] = mean
            
    column = tupla.values.tolist()
    lista = []
    for i in range(len(column)):
        lista.append(column[i][0])
    return lista