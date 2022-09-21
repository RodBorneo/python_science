#Crie um condicional que, dada uma variável, faça as operações:

#Se for número positivo, retorna "Número positivo"
#Se for número negativo, retorna "Número negativo"
#Se for zero, retorna "zero"
#Se não for número, retorna "Não é um número"


x = input("Aperte qualquer tecla: ")

if type(x) is str:
	print("Não é um número")	
elif x > 0:
	print("Número positivo")
elif x < 0:
	print("Número negativo")
elif x == 0:
	print("zero")
	
