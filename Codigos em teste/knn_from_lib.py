from fancyimpute import KNN
#X is the complete data matrix
#X_incomplete has the sema values as x except a subset have been replace with NaN values

#Use 3 nearest rows which have a feature to fill in each row's missing features 
X_filled_knn = KNN(k=3).complete(X_incomplete)