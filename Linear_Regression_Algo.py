# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 18:40:34 2017

@author: jpuri
"""

import numpy as np
import matplotlib.pyplot as mlib


class LinearRegression:
    def est_coff(self,x,y):
        #size of the array
        n = np.size(x)
        #mean of the array
        m_x = np.mean(x)
        m_y = np.mean(y)
        #now standard and cross deviation of x and y
        SS_xy = np.sum(y*x - n*m_x*m_y)
        SS_xx = np.sum(x*x - n*(m_x*m_x))
        #getting the values of coeff B0 and B1
        B_1 = SS_xy/SS_xx
        B_0 = m_y - B_1*m_x
        
        return (B_0,B_1);
    def plot_regression(self,x,y,b):
        #plot the points
        mlib.scatter(x,y,color = "m",
               marker = "o", s = 30)
        #predicted
        y_pred = b[0] +b[1]*x
        
        #plot the line
        mlib.plot(x,y_pred,color="g")
        # putting labels
        mlib.xlabel('x')
        mlib.ylabel('y')
 
        # function to show plot
        mlib.show()
    def run(self):
        # observations
        x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
        B = self.est_coff(x,y)
        self.plot_regression(x, y, B)
 

def main():
        reg = LinearRegression()
        reg.run();
    
if __name__ == "__main__":
    main()