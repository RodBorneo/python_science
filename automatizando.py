#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 22:08:42 2022

@author: rodrigoborneo
"""

Path = '/Users/rodrigoborneo/Documents/Python/Py_Eng_Cien/Sec_1/Arquivos_teste/teste_'

test_numbers = list(range(1,6))

for i in test_numbers:
    file_name = Path + str(i) + '.txt'
    print(file_name)
    
    
with open(file_name) as f:
    linhas = f.readlines()
    f.close
    
#metodo index identifica a posição do primeiro elemento da lista que possui a string especificada
linhas.index('TESTE\n')
#como o 'TESTE\n' está no indice 5, deve buscar tudo que está no 6 para frente
linhas[6:]



arquivo_full = ['ID,A,B\n']
for i in test_numbers:
    file_name = Path + str(i) + '.txt'
    with open(file_name) as f:
        linhas = f.readlines()
        f.close
        
    arquivo_full.extend(linhas[7:])


text = ''
for i in enumerate(arquivo_full):
    text += arquivo_full[i[0]]
    
    
new_file = '/Users/rodrigoborneo/Documents/Python/Py_Eng_Cien/Sec_1/Arquivos_teste/ARQUIVO_FULL.txt'

with open(new_file, 'w') as f:
    f.write(text)
    f.close
    
    
    
    
