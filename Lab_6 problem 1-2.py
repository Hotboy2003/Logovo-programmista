# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:21:11 2019

@author: admin
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
t = np.arange(-10, 10, 0.1)
R = 3
x=R*(t - np.sin(t))
y=R*(1-np.cos(t))
plt.plot(x,y)
plt.show()

def astroida(R=1):
    t = np.arange(-10, 10, 0.1)
    x = R*np.cos(t)**3
    y = R*np.sin(t)**3
    plt.plot(x,y)
    plt.show()
astroida()




fig, ax = plt.subplots()
ball, = plt.plot([],[], 'o')
def circle_move(R, t):
    x = R*np.cos(t)**3
    y = R*np.sin(t)**3
    return x,y
edge = 3
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data(circle_move(R=2, t = i))

ani=FuncAnimation(fig, animate, frames = np.arange(-10, 10, 0.1), interval = 100)
ani.save('animate.gif')



fig, ax = plt.subplots()
ball, = plt.plot([],[], 'o')
def cicloida(R, t):
    x = R*(t-np.sin(t))
    y = R*(1-np.cos(t))
    return x,y
edge = 30
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data(cicloida(R=3, t = i))

ani=FuncAnimation(fig, animate, frames = np.arange(-10, 10, 0.1), interval = 30)
ani.save('animate2.gif')