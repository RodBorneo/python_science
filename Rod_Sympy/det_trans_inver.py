#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 20:07:10 2022

@author: rodrigoborneo
"""
"""
Dadas as matrizes A,B, C e D, calcule, para cada uma, 
- > o determinante, 
-> a matriz transposta 
-> a matriz inversa.
"""

import sympy as sp
sp.init_printing()

A = sp.Matrix([[1,2],[4,5]])
B = sp.Matrix([[sp.cos(sp.pi/4), -sp.sin(sp.pi/4)],[sp.sin(sp.pi/4), sp.cos(sp.pi/4)]])
C = sp.Matrix([[2, -2],[-2, 5]])
D = sp.Matrix([[2, 2],[4,4]])

A.det()
A.T
A**-1

B.det()
B.T
B**-1

C.det()
C.T
C**-1

D.det()
D.T
#retorna um erro pois Matrix det == 0; not invertible.
D**-1
