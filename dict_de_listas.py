#Crie um dicionário que correlacione as seguintes listas:

valores = [1,2,3,4,5]
keys = ['a','b','c','d','e']

dict = {}

if len(valores) == len(keys):

	for k in range(len(valores)):
		dict[valores[k]] = keys[k]
else:
	print("listas de tamanho diferente")

print(dict)		