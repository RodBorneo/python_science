#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 18:08:05 2022

@author: rodrigoborneo
"""


"""
A função map pode ser usada em 2 casos para converter uma lista em uma string.

> se a lista contiver apenas números.
> Se a lista for heterogênea

A função map() aceitará 2 argumentos;

     função str(); que converterá o tipo de dados fornecido no tipo de dados string.
     Uma sequência iterável; cada elemento na sequência será chamado pela função str().
     Os valores de string serão retornados por meio de um iterador.

No final, a função join() é usada para combinar todos os valores 
retornados pela função str().

"""
#Crie uma função que lê um arquivo de extensão .txt e 
#retorne quantas palavras tem esse arquivo.

file_path = '/Users/rodrigoborneo/Documents/Python/Py_Eng_Cien/Sec_1/frase_contar.txt'

print("----------------com readlines()---------------")


with open(file_path,encoding="utf-8") as f:
#O método readlines() retorna uma lista contendo cada linha do arquivo como um item de lista.
    f_data = f.readlines()
    f.closed
    
print("f_data é:", f_data)

#O método join() pega todos os itens em um iterável e os une em uma string.
#A função str() converte o valor especificado em uma string.
lista_em_string = ' '.join(map(str, f_data))

#a mesma coisa só que usando um laço for
lista_em_string2 = ''
for palavra in f_data:
    lista_em_string2 += ''+ palavra



def contar_palavras(frase):
    lista_palavras = frase.split(' ')
    num_palavras = len(lista_palavras)
    return num_palavras

a = contar_palavras(lista_em_string)
print(a)

b = contar_palavras(lista_em_string2)
print(b)

"""
Obs.: caso haja "\n" no arquivo .txt, uma boa forma de corrigir isso é
utilizando 

var = string.replace('\n','')
"""