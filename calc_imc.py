#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 19:23:04 2022

@author: rodrigoborneo
"""

import modulo_calc_imc as imc

meu_peso = 72
minha_altura = 1.85

a = imc.calc_imc(meu_peso, minha_altura)
print(a)