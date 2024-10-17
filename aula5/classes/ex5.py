"""

"""


def imprimir(niveis:int):
    for y in range(niveis):
        for x in range(y+1):
            print(x+1, end="  ")
        print("")
imprimir(int(input("Quantos níveis quer: ")))