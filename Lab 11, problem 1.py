# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:17:45 2019

@author: admin
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

t = np.arange(0, 100, 1)
m = 1
F1 = 1
F2 = 2
F3 = 3
F4 = 1

def idk(z, t):
    x, v_x, y, v_y = z
    dxdt = v_x
    dv_xdt = np.cos(np.pi/ 6) * F2 + np.cos(np.pi / 6) * F3 + F4
    dydt = v_y
    dv_ydt = np.cos(np.pi / 6) * F2 + np.sin(np.pi / 6) * F3 + F1
    return dxdt, dv_xdt, dydt, dv_ydt

x0 = 0
v_x0 = -100
y0 = 0
v_y0 = -100
z0 = x0, v_x0, y0, v_y0

solve = odeint(idk, z0, t)

fig = plt.figure()
massive = []

for i in range(0, len(t), 1):
    ball, = plt.plot(solve[:i, 0], solve[:i, 2])
    ball_line, = plt.plot(solve[i,0], solve[i, 2])
    massive.append([ball, ball_line])
    
ani = ArtistAnimation (fig, massive, interval = 50)
plt.axis('equal')
ani.save('lab11.gif')

    
    
