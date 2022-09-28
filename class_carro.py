#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:49:37 2022

@author: rodrigoborneo
"""

class carro:
    def __init__(self, cor_do_carro, marca_do_carro, ano_do_carro):
        self.cor = cor_do_carro
        self.marc = marca_do_carro
        self.ano = ano_do_carro
        self.donos = []
        
    def add_dono(self,novo_dono):
        self.donos.append(novo_dono)
        
        
meu_carro = carro('preto','VW', 2012)
meu_carro.add_dono('Rodrigo')

meu_carro.donos