#Crie uma lista com os cinquenta primeiros números primos.
#Dica: pode ser utilizado o comando break e continue
	
#--------------------------------------
lista_primos = [2]
prox_num = 2

while len(lista_primos) < 50:
	prox_num += 1
	prox_num_status = ''
	
	for num in lista_primos:
		quociente = prox_num / num
		quociente_inteiro = prox_num // num

		if quociente_inteiro == quociente:
			prox_num_status = 'pula'
			break

	if prox_num_status == 'pula':
		continue
	else:	
		lista_primos.append(prox_num)

print(lista_primos)
