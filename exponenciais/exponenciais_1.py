# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:19:27 2020

@author: David
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import array

# 100 linearly spaced numbers
x = np.linspace(-5,5,100)

# Define a row vector
v = array([-5, -4, -3 , -2,-1, 0, 1, 2, 3 ,4 ,5])

# the function, which is y = x^2 here

# setting the axes at the centre
fig = plt.figure()

# plot the function
plt.plot(x,pow(3,x), 'r')

# show the plot
plt.show()

