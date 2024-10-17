"""
Peça ao utilizador 10 valores numéricos inteiros
Verique se o valor numérico inteiro, descarte esse valor
Adicione a lista os valores numéricos
Calcule a media dos valores na lista
"""

lista = []

for i in range(10):
    val = "x"
    while not val.isnumeric():
        val = input("Introduza um valor numérico: ")
        if not val.isnumeric():
            print("Não é um valor numérico, repita.")
        else:
            lista.append(val)
print(lista)