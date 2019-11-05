# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:04:56 2019

@author: admin
"""

import matplotlib.pyplot as plt
import numpy as np
plt.plot([1,1,5,5,1],[1,5,5,1,1], marker='o', color='k', ms='10')
plt.show()

def parabolla_plotter(a=1, b=1, c=0):
    x=np.arange(-10,10,0.01)
    y=a*x**2+b*x+c
    plt.plot(x,y)
    plt.show()
parabolla_plotter()

def gyperbola_plotter(k=1):
    x=np.arange(1,10,0.01)
    y=k/x
    plt.plot(x,y)
    plt.show()
gyperbola_plotter()

def ellips_plotter(a=5, b=5):
    x=np.arange(-10,10,0.01)
    y=np.arange(-10,10,0.01)
    X,Y=np.meshgrid(x,y)
    fxy=X**2/a**2+Y**2/b**2
    plt.contour(X,Y,fxy,levels=[1])
    plt.show()
ellips_plotter()

def circle_plotter(R=1):
    x=np.arange(-10,10,0.01)
    y=np.arange(-10,10,0.01)
    X,Y=np.meshgrid(x,y)
    fxy=X**2+Y**2
    plt.contour(X,Y,fxy,levels=[R])
    plt.show()
circle_plotter() 
    
    

