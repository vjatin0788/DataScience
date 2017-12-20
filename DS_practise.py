# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:35:40 2017

@author: jpuri
"""

# Tutorial for data science

import numpy as np
import pandas as pd
import matplotlib as plt

data = pd.read_csv('pokemon.csv')
data.info()
data.head(5)
data.columns

#info about matplotlib
#Line plot
Speed = data.Speed # Access the particular column of the dataFrame it is type of series
Defense = data.Defense
print(Defense)
Speed.plot(kind = 'line', color = 'g',label = 'Speed',linewidth=1,alpha = 0.5,grid = True,linestyle = ':')
Defense.plot(kind = 'line', color = 'r',label = 'Speed',linewidth=1,alpha = 0.5,grid = True,linestyle = ':')
plt.legend(loc='upper right')     # legend = puts label into plot
plt.xlabel('x axis')              # label = name of label
plt.ylabel('y axis')
plt.title('Line Plot')            #title 

#Scatter plot
data.plot(kind='scatter', x='Attack', y='Defense',alpha = 0.5,color = 'red')
plt.xlabel('Attack')              # label = name of label
plt.ylabel('Defence')
plt.title('Attack Defense Scatter Plot')    

#histogram
data.Speed.plot(kind='hist',bins=50,figsize = (15,15))

#dictionaries
dictionary = {'one':'hello','two':'world'}
print(dictionary.keys())
print(dictionary.values())
print(type(dictionary['one']))
dictionary['one'] = 'jatin' #override
dictionary['three'] = 'world' #insert new key value
print(dictionary)
del dictionary['three'] # delete the element
print('one' in dictionary) #check wheather key exist or not
dictionary.clear() 
del dictionary #same as above

for key,value in dictionary.items():
    print(key,':',value)
#intro to pandas
print(type(Speed)) #Series type
dataFrame = data[['Defense','Attack']] #dataframe type is 2d array
print(type(dataFrame))
#filtering pandas dataframe
X = data['Defense'] >200
print(type(X)) #series type containing the boolean value for each record
print(type(data[X])) #it will return the record containing true values.
print(Defense) 
#filtering the logical
print(data[np.logical_and(data['Defense'] >200,data['Attack'] >100)])
#or
print(data[(data['Defense']>200) & (data['Attack']>100)])
print(type(data['Speed'])) #series type is 1d array

#for looping
list =[2,3,4] #list
lis = {2,3,4} #set
print(type(list))
for key,value in enumerate(list):
    print(key,':',value)