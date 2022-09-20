#Dado um número inteiro, faça um operador while que 
#calcule o fatorial desse número. 
#Dicas: utilize as operações ** =* e também -=

x = int(input("Digite um número inteiro: "))
fact_x =1

while x > 0:

	fact_x *= x
	x -=1
print(fact_x)
