#Faça um loop for para criar uma lista que intercale os valores das listas a seguir:

#valores = [1,2,3,4,5]
#['a','b','c','d','e']

valores = [1,2,3,4,5]
letras = ['a','b','c','d','e']

intercalada = []

#O método append() anexa um elemento ao final da lista.
for i in range(len(valores)):
	intercalada.append(valores[i])
	intercalada.append(letras[i])

print(intercalada)    