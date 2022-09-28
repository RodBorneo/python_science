#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:50:36 2022

@author: rodrigoborneo
"""

class vetor_2d:
    def __init__(self,vec_x,vec_y):
        self.x = vec_x
        self.y = vec_y
        
    def norma(vet):
        return ((vet.x**2 + vet.y**2)**(1/2))
    
    def __add__(vet_1,vet_2):
        return vetor_2d(vet_1.x + vet_2.x, vet_1.y + vet_2.y)
    
v1 = vetor_2d(2,3)
v2 = vetor_2d(4,5)

v3 = v1 + v2
print(v3.x)
print(v3.y)
v3.norma()