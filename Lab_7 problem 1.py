# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:45:14 2019

@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
fig = plt.figure()
def circle_func(x_centre_point, y_centre_point, R, N):
    x_coord = np.linspace(-5, 5, 100)
    y_coord = np.zeros(100)
    for i in range(0, N, 1):
        alpha = np.linspace(0, 2*np.pi, N)
        x_coord[i] = x_centre_point + R*np.cos(alpha[i])
        y_coord[i] = y_centre_point + R*np.sin(alpha[i])
    return x_coord, y_coord
R = 1
parabolla_x = np.arange(-5, 5, 1)
parabolla_y = parabolla_x**2 + parabolla_x
x_centre_move =  np.linspace(-5, 5, 100)
y_centre_move = x_centre_move**2 + x_centre_move
anim_list = []
N = 100
for i in range(0,N,1):
    x_coord, y_coord = circle_func(x_centre_move[i], y_centre_move[i], R=R, N=N)
    circle, = plt.plot(x_coord, y_coord,'g-')
    parabolla, = plt.plot(parabolla_x[:i+1], parabolla_y[:i+1], 'r-')
    point, = plt.plot(parabolla_x, parabolla_y, 'bo')
    anim_list.append([circle, parabolla, point])

plt.axis('equal')    
ani = ArtistAnimation(fig, anim_list, interval =50)
ani.save('parabolla.gif')
    