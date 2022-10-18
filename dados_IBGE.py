#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 00:43:22 2022

@author: rodrigoborneo

Importar a tabela dos 100 maiores municípios em relação ao PIB 

Quantos municípios estão no estado de São Paulo?
Qual a participação acumulada desses municípios?

"""

file_path = '/Users/rodrigoborneo/Documents/Python/Python-para-Engenheiros-e-Cientistas/Notebooks/arquivos_auxiliares/PIB_100_maiores_cidades_2017.txt'

with open(file_path,encoding='latin-1') as f:
#readline retorna uma lista onde cada elemento é uma linha do arquivo
    f_data = f.readlines()
    f.closed

linhas = []

for i in range(len(f_data)):
    linhas.append(f_data[i].split(','))
    
colunas_dict = {}

for key in linhas[0]:
    colunas_dict[key] = []
    
    colunas_n = linhas[0].index(key)
    
    for i in range(1,len(linhas)): #começa no 1 que é para não pegar a palavra Estado
        colunas_dict[key].append(linhas[i][colunas_n]) #permite passar pelas keys buscando as informações
        
lista_estados = colunas_dict.get('Estado') #é o mesmo que fazer um colunas_dict['Estado']
num_municipios_sp = lista_estados.count('SP')

PIB_acm_SP = 0

for i in range(len(colunas_dict['Estado'])):
    if colunas_dict['Estado'][i] == 'SP': #entra na chave estado e para cada linha pega o valor Estado
        PIB_acm_SP += float(colunas_dict['Participação (%)'][i])#caso o estado seja SP, soma a 'Particpação (%)
    
print(num_municipios_sp)
print(PIB_acm_SP)