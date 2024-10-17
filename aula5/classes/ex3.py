from random import randint
from Quadrado import Quadrado

"""

1 - Crie 400 quadrados com lado aletatorios
2 - Indique o que tem a maior area 
3 - Indique o que tem a menor area

"""

quadrados : list[Quadrado] = []

for i in range(400):
    quadrados.append(Quadrado(randint(1, 100), "Amarelo"))

maior_area = 0
menor_area = 0

for i in range(1, len(quadrados)):
    area = quadrados[i].area() 
    if area > quadrados[maior_area].area():
        maior_area = i
    if area < quadrados[menor_area].area():
        menor_area = i

print(f"O quadrado com a menor área está no indice nº{menor_area} e tem {quadrados[menor_area].area()} de área")
print(f"O quadrado com a maior área está no indice nº{maior_area} e tem {quadrados[maior_area].area()} de área")