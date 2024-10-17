import random

print(random.randint(1,10000))

# Crie uma lista com 1000 números inteiros aleatórios
# Imprima o valor todos os valores da lista multiplicados pela posição
# Exemplo:
# lista -> [3,4,5,10]
# ouput:
# 0
# 4
# 10
# 

lista = []

for i in range(1000):
    lista.append(random.randint(1,10000) * i)
print(lista)