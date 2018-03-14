import lidaExcel
import statistical
import copy
from knn_final import knn_impute
from KMeans import KMeansInterface
from DBScan import DBScanInterface
from hierarchical import HierarchicalInterface

##############################################################################
print("Hello. This is a simple control for users\n")
print("We have some training datasets for your tests, they are: \n1 - Wine\n2 - Balance\n3 - Iris\n4 - Glass\n5 - Breast Cancer Winsconsin\n")
name = int(input("Select your training dataset :"))

if(name == 1):
    path = 'Datasets/wine.xlsx'
    name = 'wine'
elif(name  == 2):
    path = 'Datasets/balance.xlsx'
    name = 'balance'
elif(name == 3):
    path = 'Datasets/iris.xlsx'
    name = 'iris'
elif(name  == 4):
    path = 'Datasets/glass.xlsx'
    name = 'glass'
elif(name  == 5):
    path = 'Datasets/cancer.xlsx'
    name = 'cancer'
    

ds = lidaExcel.leMatriz(path, name)
print("You choose: %s\n" % name)

rate = float(input("Now, choose the rate of MV in the training dataset: "))
mv = lidaExcel.geraMissingValues(ds,rate)
lidaExcel.gravaNovaAba(mv,path,"MV")
print("Sheet stored in %s.xlsx\n" %name)
print("####################################################################\n")
print("We have 5 imputations methods:\n1 - Mean\n2 - Mode\n3 - Median\n4 - Deviation\n5 - KNN\n")

sheetCount = 5


mv1 = copy.deepcopy(mv)
matrix = statistical.imputationMean(mv1)
lidaExcel.gravaNovaAba(matrix,path,"Mean")

matrix = statistical.imputationMode(mv)
lidaExcel.gravaNovaAba(matrix,path,"Mode")

mv2 = copy.deepcopy(mv)
matrix = statistical.imputationMode(mv2)
lidaExcel.gravaNovaAba(matrix,path,"Median")

matrix = statistical.imputationDesvioPadrao(mv)
lidaExcel.gravaNovaAba(matrix, path, "Deviation")

matrix = [knn_impute(reg,mv,3,"mean") for reg in mv]      
lidaExcel.gravaNovaAba(matrix,path,"KNN")
    
print("You imputed the rate of %d" %rate)

#We'll now apply clustering methods on each sheet of dataset
print("We have 3 clustering methods:\n1 - KMeans\n2 - DBScan\n3 - Hierarchical\n")
clustering = int(input("Enter with a number of clustering method (press 0 to exit loop): "))
print("We'll apply the clustering method on all sheets of dataset")

while(clustering!=0):
    if clustering == 1:
        for i in range(2, sheetCount+1):
            print("For the sheet %d\n", i)
            KMeansInterface(path, i)
    elif clustering == 2:
        for i in range(1, sheetCount):
            DBScanInterface(path, i)
    elif clustering == 3:
        for i in range(1, sheetCount):
            HierarchicalInterface(path, i)
    clustering = int(input("Choose again or press 0 to exit loop: "))
