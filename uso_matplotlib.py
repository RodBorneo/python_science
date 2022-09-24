#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 14:28:48 2022

@author: rodrigoborneo
"""

import matplotlib.pyplot as plt

x = [x for x in range(101)]
y = [y**2 for y in x]

plt.plot(x,y, '+')

plt.xlabel('x')
plt.ylabel('y')

#raiz quadrada sem import math

a = 4**(1/2)
print(a)

#raiz quadrada com import math

from math import sqrt

b = sqrt(4)
print(b)