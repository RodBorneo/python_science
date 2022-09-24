"""
Utilizando somente uma linha de programação, crie uma lista que contenha 
os números ímpares de 1 a 51.
"""
"""
A função range() tem como padrão 0 como valor inicial, 
porém é possível especificar o valor inicial adicionando um parâmetro: 
range(2, 6), que significa valores de 2 a 6 (mas não incluindo 6):
"""
lista_impares = lista_impares = [(i*2 + 1) for i in range (26)]
print(lista_impares)

#lambda x: função_x 	Retorna uma função
f_impares = lambda x: (x*2+1)	
lista_impares_V2 = [f_impares(n) for n in range(26)]
print(lista_impares_V2)