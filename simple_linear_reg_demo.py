# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:41:03 2017

@author: jpuri
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Importing the dataset
#os.getcwd()
#os.chdir('D:\\Users\\jpuri\\Desktop\\My Work\\\Machine Learning A-Z\\Part 2 - Regression\\Section 4 - Simple Linear Regression')
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values #matrix of 2D is required (Experience)
y = dataset.iloc[:, 1].values #vector of 1D is required because it is dependent variable.(Salary)

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

#fitting the linear regression model in the training set.
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

#predicting the salary on test case
y_pred = regressor.predict(X_test)

#plotting the training observaion
plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='green')
#plt.plot(X_test,y_pred,color='green')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()
#plotting the test observation
plt.scatter(X_test,y_test,color='red')
plt.plot(X_train,regressor.predict(X_train),color='green') #becase our model is trained on the 
#plt.plot(X_test,y_pred,color='green')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()
