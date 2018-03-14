import math 
import copy

def imputationMean(matriz):

    #itero sobre cada coluna crio uma media com valor 0 inicial

    for coluna in range(len(matriz[1])):
        media = 0.0
        qtdRegistros = 0
        #itero sobre as linhas
        for i in range(len(matriz)):
            if matriz[i][coluna] != "MISSING":
                media = media + float(matriz[i][coluna])
                
                qtdRegistros = qtdRegistros + 1

        media = media/qtdRegistros

        for i in range(len(matriz)):
            if matriz[i][coluna] == "MISSING":
                matriz[i][coluna] = media
    return matriz
                

def imputationMode(matriz):
    matriz1 = copy.deepcopy(matriz)
    for coluna in range(len(matriz1[1])):
        lista = []
        quantidade = 0
        moda = 0
        aparece = 0
        
#        for i in [item[coluna] for item in matriz]:
#            lista.append(i)
        for i in range(len(matriz1)):
            if(matriz1[i][coluna]!="MISSING"):
                lista.append(matriz1[i][coluna])
        
        for i in lista:                                                                              
            aparece = lista.count(i)
            if aparece > quantidade:
                quantidade = aparece
                moda = i
        #imputando a moda
        for i in range(len(matriz1)):
            if matriz1[i][coluna] == "MISSING":
                matriz1[i][coluna] = moda
    return matriz1
                
        
def imputationMedian(matriz):
    matriz2 = copy.deepcopy(matriz)
    mediana = []
    for coluna in range(1,len(matriz2[1])+1):   
        lista = []
        for i in range(0,len(matriz2)):
            if matriz2[i][coluna-1]!="MISSING":
                lista.append(float(matriz2[i][coluna-1]))
        lista.sort()
        
        if len(lista)%2==0:
            mediana.append((float(lista[int(len(lista)/2)]) + lista[int((len(lista)+2)/2)])/2)
            
        else:
            mediana.append(float(lista[int((len(lista)+1)/2)]))
            
    for coluna in range(1,len(matriz2[1])+1):
        for i  in range(0,len(matriz2)):
            if matriz2[i][coluna-1] == "MISSING":
                matriz2[i][coluna-1] = mediana[coluna-1]
    return matriz2
        
def imputationDesvioPadrao(matriz):
    
    matriz1 = copy.deepcopy(matriz)
    for coluna in range(1,len(matriz1[1])+1): #paracadacoluna
        media = 0.0
        qtdRegistros = 0
        for i in range(0,len(matriz1)):
            if matriz1[i][coluna-1] != "MISSING":
                media = media + float(matriz1[i][coluna-1])
                qtdRegistros = qtdRegistros + 1

        media = media/qtdRegistros

        desvioPadrao = 0
        somatorio = 0
        for i in range(0,len(matriz1)):
            if matriz1[i][coluna-1] != "MISSING":
                somatorio = somatorio + pow(float(float(matriz1[i][coluna-1]) - float(media)),2.0)

        desvioPadrao = somatorio/qtdRegistros
        desvioPadrao = math.sqrt(desvioPadrao)

        for i in range(0,len(matriz1)):
            if matriz1[i][coluna-1] == "MISSING":
                matriz1[i][coluna-1] = desvioPadrao
    return matriz1
