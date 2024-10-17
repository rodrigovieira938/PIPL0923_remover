def soma(v1,v2):
    return v1+v2


def soma_v2(v1: int,v2: int) -> int:
    return v1+v2

def soma_v2_1(v1: int,v2: int):
    soma = v1+v2
    print(soma)

s = soma_v2("foo", "boo")
s = soma_v2_1(12,123)