def ola_mundo():
    print("Olá Mundo")
def ola_mundo_v2(nome):
    print("Olá Mundo,", nome)
def ola_mundo_v3(nome:str, ano:int):
    print(f"Olá Mundo, {nome}, {ano}")
ola_mundo()
ola_mundo()
ola_mundo()
ola_mundo()

ola_mundo_v2("Rodrigo")
ola_mundo_v2("Rui")
ola_mundo_v2("Ana")

num = 12

ola_mundo_v3("Rodrigo", 2000)

def soma(v1: int, v2: int) -> int:
    return v1 + v2

res = soma(3,4)
print(res)

res2 = soma(3.5,4.5)
print(res2)

res3 = soma("3.5","4.5")
print(res3)