#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 13:10:10 2022

@author: rodrigoborneo
"""


#Dada a equação da cirunferência, faça o gráfico.
#(𝑥−𝑎)2+(𝑦−𝑏)2=𝑟2,𝑟=100,𝑎=100,𝑏=100

from math import sqrt

a,b,r = 100, 100, 100

x = []
y = []

#para cobrir todo o diametro da circunferencia d = 2*r
x = [i for i in range(2*r + 1)]

#isolando y da equação (x-a)**2 passa negativo, r**2 já está do outro lado
#passa a raiz quadrada e então o b passa positivo
y_de_x = lambda x: sqrt((r**2) - (x-a)**2) + b


#lembrando que tem a raiz quadrada positiva e a negativa
y_de_x_negativo = lambda x: -sqrt((r**2) - (x-a)**2) + b

#adiciona  y_de_x e x para a lista y
y.extend(list(map(y_de_x, x)))

#adiciona  y_de_x_negativo e x para a lista y
y.extend(list(map(y_de_x_negativo, x)))


x.extend(x)

#importa o matplotlib
import matplotlib.pyplot as plt

#plota o gráfico
plt.plot(x,y)