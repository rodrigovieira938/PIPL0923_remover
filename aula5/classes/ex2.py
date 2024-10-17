from Quadrado import Quadrado

"""

1 - Crie 4 Quadrados 
2 - indique o que tem a maior área

"""


quadrados = [
    Quadrado(2, "Amarelo"),
    Quadrado(4, "Amarelo"),
    Quadrado(8, "Amarelo"),
    Quadrado(16, "Amarelo")
]
areas = [q.area() for q in quadrados]

maior_area = areas[0]
indice = 0
for i in range(1, len(areas)):
    area = areas[i]
    if area > maior_area:
        indice = i
        maior_area = area

print(f"O quadrado com a maior área é o nº{indice+1}")