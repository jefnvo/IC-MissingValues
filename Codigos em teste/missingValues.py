import numpy
from pandas import read_csv

dataset = read_csv('pima-indians-diabetes.csv', header=None)
print("antes", dataset.shape)
#marcamos a quantidade de valores ausentes em certas colunas
print((dataset[[1,2,3,4,5]]==0).sum())

#marcamos os valores zero como NaN
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, numpy.NaN)
print("contamos o numero de NaN em cada coluna\n")
print(dataset.isnull().sum())

#primeira estrategia: eliminamos os valores ausentes (metodod menos aconselhado)
dataset.dropna(inplace=True)
print("depois", dataset.shape)
#segunda estrategia: substituir valores ausentes pela media das colunas
dataset.fillna(dataset.mean(), inplace=True)
#contamos o numero de MV apos essa troca
print(dataset.isnull().sum())