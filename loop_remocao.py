"""
Dada a lista ['P','A','Y','A','T','A','H','O','N'], conte o número de variáveis 'A' 
e utilize um loop para remover todos os 'A' excedente.
"""
Lista = ['P','A','Y','A','T','A','H','O','N']
print(Lista)

count_A = 0
for x in Lista:
  if x == 'A':
    count_A += 1
    Lista.remove(x)
    
print(count_A)
print(Lista) 