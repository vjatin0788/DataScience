# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:37:18 2017

@author: jpuri
"""
#import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as mplot

#import the dataframes
#self keywords are provided automatically to access the attributes of class in method
dataset = pd.read_csv("Data.csv");
X = dataset.iloc[:,:-1].values; #matrices independent variables
Y = dataset.iloc[:,3].values; #dependent variable vector

#import the library for preprocessing & handling missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN",strategy="mean",axis=0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3]) #does not include upper bound in array

#import the same library for categorising
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
#Encoding X and Y
Encoder_X = LabelEncoder()
X[:,0] = Encoder_X.fit_transform(X[:, 0])
Encoder_Y = LabelEncoder()
Y = Encoder_Y.fit_transform(Y)
#Hot Encoding the YES and NO values
#Methods argument are called dynamically . you can give any no of argument acc to requirement.
hotEncoder = OneHotEncoder(categorical_features=[0]) #dummy variables
X = hotEncoder.fit_transform(X).toarray()

#Creating the two sets Training set and test set
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 0)

#Scaling the idependent matrices
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
X_train = sc_x.fit_transform(X_train) #the train is need to fit and transform but the test
X_test = sc_x.transform(X_test)#test does not need to fit only transform . so that it transform in same manner. 
