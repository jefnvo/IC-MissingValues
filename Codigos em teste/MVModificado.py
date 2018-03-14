import lidaExcel
#from knn_final import knn_impute
import statistical
import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist




def main():
    path = 'Datasets/wine.xlsx'
    matriz = lidaExcel.leMatriz(path,'wine')#copio os dados do excel
    
    lidaExcel.geraMissingValues(matriz,0.1) #gero MV na matriz
    lidaExcel.gravaNovaAba(matriz,path,"MV")#gravo essa matriz em uma nova folha do excel
    
   
    matriz = []
    matriz = lidaExcel.leMatriz(path,'MV')
    statistical.imputationMode(matriz)
    lidaExcel.gravaNovaAba(matriz,path,"Mode")
    
    matriz = []
    matriz = lidaExcel.leMatriz(path,'MV')
    statistical.imputationMean(matriz)
    lidaExcel.gravaNovaAba(matriz,path,"Imputation Media")
    
    matriz = []
    matriz = lidaExcel.leMatriz(path,'MV')
    statistical.imputationDesvioPadrao(matriz)
    lidaExcel.gravaNovaAba(matriz,path,"Deviation")
    
    matriz = []
    matriz = lidaExcel.leMatriz(path,'MV')
    statistical.imputationMedian(matriz)
    lidaExcel.gravaNovaAba(matriz,path,"Median")
    
    matriz=[]
    matrix=[]
    matriz = lidaExcel.leMatriz(path,'MV')
    matrix = [knn_impute(reg,matriz,3,"mean") for reg in matriz]        
    lidaExcel.gravaNovaAba(matrix,path,"KNN")
    

main()