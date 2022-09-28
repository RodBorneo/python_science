#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 23:36:52 2022

@author: rodrigoborneo
"""

old_file = '/Users/rodrigoborneo/Documents/Python/Py_Eng_Cien/python_science/Arquivo_sujo.txt'
with open(old_file) as f:
    linhas = f.read()
    f.close
    
#no replace o 1º argumento é oq vai ser substituido o 2º é oq substitui
linhas_new = linhas.replace('p','').replace(' ','')
print(linhas_new)

new_file = 'Arquivo_limpo.txt'

with open(new_file, 'w') as nf:
    nf.write(linhas_new)
    nf.close
