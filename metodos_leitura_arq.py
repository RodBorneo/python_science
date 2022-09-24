#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 14:50:16 2022

@author: rodrigoborneo
"""

# A ser resolvido (assita a vídeo aula com a resolução)

file_path = '/Users/rodrigoborneo/Documents/Python/Python-para-Engenheiros-e-Cientistas/Notebooks/arquivos_auxiliares/teste.txt'

print("----------------com readlines()---------------")
with open(file_path,encoding="utf-8") as f:
#O método readlines() retorna uma lista contendo cada linha do arquivo como um item de lista.
    f_data = f.readlines()
    f.closed
    
    
lista_colunas = f_data[0].split('!') 

print("f_data é:", f_data)
print("lista é: ",lista_colunas)


print('')
print('')
print("----------com read()---------------")
with open(file_path,encoding="utf-8") as f:
#O método read() retorna o número especificado de bytes do arquivo. O padrão é -1, o que significa que o arquivo inteiro
  f_data2 = f.read()
  f.close

lista_colunas2 = f_data2.split('!') 

print("f_data2 é:", f_data2)
print("lista2 é:", lista_colunas2)

print('')
print('')
print("---------------com readline()-------------")

with open(file_path,encoding="utf-8") as f:
#O método readline() retorna uma linha do arquivo.
    f_data3 = f.readline()
    f.closed
    
lista_colunas3 = f_data3.split('!')   
print("f_data3 é:", f_data3)
print("lista3 é:", lista_colunas3)
