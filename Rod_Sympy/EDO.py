#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:57:14 2022

@author: rodrigoborneo
"""

#dy/dx = x**2/y

import sympy as sp
sp.init_printing()

x = sp.symbols('x')
y_x = sp.Function('y_x')
dy_x = sp.Derivative(y_x(x),x)

edo_1 = dy_x - x**2/(y_x(x))

sp.dsolve(edo_1)