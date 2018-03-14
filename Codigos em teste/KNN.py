import csv
import random
import math
import operator
#a funcao abaixo divide o meu dataset IRIS em dois pedaços
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):#preciso conhecer o numero de atributos
                dataset[x][y] = float(dataset[x][y])
            
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
                

#calcula distancia euclidiana
def euclideanDistance(instance1, instance2, length):#length aqui pega o numero de axis
    distance = 0
    for x in range(length):
        distance+=pow(instance1[x] - instance2[x], 2)
    return math.sqrt(distance)

                
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1#pego tamanho do dataset de treino
    for x in range (len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))#armazeno a distancia
    distances.sort(key=operator.itemgetter(1))#ordene pelo atributo do segundo campo da tupla
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

def main():
    #preparando os dados
    trainingSet = []
    testSet = []
    split = 0.67
    loadDataset('iris.data', split, trainingSet, testSet)
    print('Training set: ', len(trainingSet))
    print('Test set: ', len(testSet))
    
    #gerando predicoes
    predictions=[]
    k = 3
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')
    
main()