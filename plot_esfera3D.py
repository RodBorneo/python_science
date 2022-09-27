#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 18:28:03 2022

@author: rodrigoborneo
"""

#nome_arquivo = '/Users/rodrigoborneo/Documents/Python/Py_Eng_Cien/python_science/PONTOS_ESFERA.txt'

def pega_coordenadas(nome_arquivo):
    with open(nome_arquivo) as f:
        #uma lista onde cada linha do arquivo é um elemento na lista
        f_data = f.readlines()
        f.close
    
    linhas = []

    for i in range(len(f_data)):
        #para cada linha usa o método slpit e divide pelas vírgulas
        linhas.append(f_data[i].split(','))
        
    #cria um dicionário onde as chaves são X,Y e Z a os valores são listas vazias
    #as listas são preenchidas com os valores das coordenadas
    Coordenadas = {}
    Coordenadas['X'] = [] 
    Coordenadas['Y'] = [] 
    Coordenadas['Z'] = [] 


    for i in range(len(linhas)):
        #linha i coluna 4, 5 e 6, que é onde estão os valores float no txt
        x = float(linhas[i][3])
        y = float(linhas[i][4])
        z = float(linhas[i][5])
    
        Coordenadas['X'].append(x)
        Coordenadas['Y'].append(y)
        Coordenadas['Z'].append(z)
        
    #a função pega um arquivo e retorna um dicionário    
    return Coordenadas
    

def plot_3D_coord(coord_dict):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x = coord_dict['X']
    y = coord_dict['Y']
    z = coord_dict['Z']
    
    ax.scatter(x,y,z)
    
nome_arquivo = '/Users/rodrigoborneo/Documents/Python/Py_Eng_Cien/python_science/PONTOS_ESFERA.txt'
                   
dicionario_esfera = pega_coordenadas(nome_arquivo)
plot_3D_coord(dicionario_esfera)
                  
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
