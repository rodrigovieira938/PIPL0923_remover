# Crie uma função que some todos os valores de uma lista de interios

def sum_list(lista) -> int:
    sum = 0
    for elm in lista:
        sum += elm
    return sum

lista = [1,2,3,4,5]
print(sum_list(lista))