"""
Faça uma função para imprimir:
    a altura deve ser recebido como parametro

    1
    2   2
    3   3   3
    
    ''''''   
    n   n   n   n   n   n ...n
    
"""

def ex8(altura):
    maxchars = len(str(altura))
    for x in range(1, altura+1):
        number = str(x)
        if len(number) < maxchars:
            for i in range(maxchars-len(number)):
                number = "0" + number
        for y in range(x):
            print(number, end="   ")
        print("\n")

ex8(40)