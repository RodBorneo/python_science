#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:28:49 2022

@author: rodrigoborneo
"""

def funcao1():
    print('função 1')
    
def funcao2():
    print('função 2')
    
"""
Essa estrutura do if __name == '__main__' é interessante para diferenciar quando
você roda o módulo como script diretamente ou quando você chama esse módulo
através de outro código
"""
if __name__ == '__main__':
    funcao1()
    funcao2()
    print('Este código está sendo executado como script')
else:
    print('Este código está sendo executado como módulo')