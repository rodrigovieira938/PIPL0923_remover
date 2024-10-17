"""
Faça uma func para imprimir, deve receber como param o num de niveis:

  

    1

    2   2

    3   3   3

    .....

    n   n   n   n   n   n  ... n

    

    

    Exep: 

     

     input 

     x = 3

     

     output 

    

    1

    2   2

    3   3   3

     

     

     input 

     x = 5

     

     output 

    

    1

    2   2

    3   3   3

    4   4   4   4

    5   5   5   5   5
"""

def imprimir(niveis:int):
    for y in range(niveis):
        for x in range(y+1):
            print(y+1, end="  ")
        print("")
imprimir(int(input("Quantos níveis quer: ")))