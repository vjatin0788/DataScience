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
    
#Lambda Expression
double = lambda x : x * 2
print(double(10))

#looping
df = data[['Attack']]
series = data['Attack']
print(type(df[0:3]))

#iterator and generator

class listClass:
    
    def __init__(self,max):
        self.max = max
     
    def __iter__(self):
         self.start = -1
         self.inc = 1
         return self
    def __next__(self):
        if self.start > self.max :
             raise StopIteration  
        self.start = self.start + self.inc
        return self.start
        
   for i in listClass(10):
       print(i)
       
#generators are iterators  
def customGen(max):
    a = 0
    itr =1
    for i in range(a,max,itr):
        yield i
    
gen = customGen(10)  
next(gen)      

#zip and unzip
listA = [1,2,3,4]
listB = [5,6,7,8]
listC = [5,6,7,8]
z = zip(listA,listB,listC)
print(list(z))
z_list = list(z)
#unzip
un_zip = zip(*z_list)
u_listA,u_listB,u_listC = list(un_zip)
print(u_listA)

#comprehensions in list
lis = [1,2,3,4,5,6,7,8,9,10,11,12]
temp = [i**2 if i%2 == 0 else i-2 if i>5 else i-4 for i in lis]
print(temp)

#Cleaning data
print(data['Type 1'].value_counts(dropna=False))
data.describe()
data.boxplot(column = 'Attack',by = 'Legendary')

# lets melt
# id_vars = what we do not wish to melt
# value_vars = what we want to melt
melted = pd.melt(frame=data.head(),id_vars = 'Name', value_vars= ['Attack','Defense'])

 #creating the dataframes
list1 = [1,2,3]
list2 = [4,5,6]
list_col = [list1,list2]
list_label = [7,8]
z_list =list(zip(list_label,list_col))
dict_list =  dict(z_list)
df = pd.DataFrame(dict_list)
df["capital"] = [1,2,3]
df["9"] = 0

#plotting the data
data_temp = data.loc[:,['Attack','Defense']]
data_temp.plot()
data_temp.plot(subplots = True)
data_temp.plot(kind='scatter',x='Attack',y='Defense')
data_temp.plot(kind='hist',y = 'Defense',bins=50,range = (0,250),normed =True)
fig, axes = plt.subplots(nrows=2,ncols=1) #it will generate the dummy graph and we can fit the values into it.
data_temp.plot(kind='hist',y = 'Defense',bins = 50,range =(0,250),normed =True, ax = axes[0])
data_temp.plot(kind='hist',y = 'Defense',bins = 50,range =(0,250),normed =True, ax = axes[1],cumulative = True)

#Date Time in python
data2 = data.head()
time_list = ["2018-12-2","2018-11-23","1992-03-10","1993-03-15","1993-03-16"]
date_time = pd.to_datetime(time_list)
data2['Date'] = date_time
data2 = data2.set_index('Date')
print(data2.loc['1993-03-15']) #loc always use the index to find the value. loc[row,column] or loc[row]
data2.resample("A").mean() # A for year and M for month .it is used to resample the data over time interval. we can use any function mean,median,etc
data2.resample("A").mean().interpolate('linear') # it will fill the value where it is NaN with mean value
data2.resample("A").first().interpolate('linear')

#Manuplating the dataframe with different ways
data['HP'][12:] #column name and rows
data.HP[1] #column name and rows
data.loc[:,"HP":"Defense"]
data[["Attack","Defense"]]
data.loc[10:1:-1,"HP":"Defense"] #reverse slicing


#filtering the dataframe
# Creating boolean series
boolean = data.HP > 200
data[boolean] #filtering using the boolean
# Combining filters
first_filter = data.HP > 150
second_filter = data.Speed > 35
data[first_filter & second_filter]
# Filtering column based others
data.HP[data.Speed<15]

#Transforming the data
#using the simple pyhton function
def div(n):
    return n/2
data.HP.apply(div)
# Or we can use lambda function
data.HP.apply(lambda n : n/2)
# Defining column using other columns
data["total_power"] = data.Attack + data.Defense
data.head()


#Hierarichal indexing
data4 =data3.set_index(["Type 1","Type 2"]) #it will create index from two column
data4.loc["Fire","Flying"] #it will call the index
