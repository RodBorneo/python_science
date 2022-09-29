#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 22:40:21 2022

@author: rodrigoborneo
"""

Path = '/Users/rodrigoborneo/Documents/Python/Py_Eng_Cien/Sec_1/Arquivos_teste/teste_'

Test_numbers = list(range(1,6))

for i in Test_numbers:
    file_name = Path + str(i) + '.txt'
    print(file_name)
    
    
import pandas as pd
    
DF_list = []

for i in Test_numbers:
    file_name = Path + str(i) + '.txt'
#skiprows serve para pular as 6 primeiras linhas onde há informação dispensável
    DF_list.append(pd.read_csv(file_name,skiprows= 6))
    
#olhar 9.5
concat_DF = pd.concat(DF_list)

'''
Converte para CSV
csv_file = '/Users/rodrigoborneo/Documents/Python/Py_Eng_Cien/Sec_1/Arquivos_teste/tARQUIVO_FULL.csv'
concat_DF.to_csv(csv_file)


Converte para Excel
excel_file ='/Users/rodrigoborneo/Documents/Python/Py_Eng_Cien/Sec_1/Arquivos_teste/tARQUIVO_FULL.xlsx'
concat_DF.to_excel(excel_file)
'''