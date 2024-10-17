class Circulo:
    def __init__(self,raio:int, cor:str):
        self.raio = raio
        self.cor = cor

class Trapezio:
    def __init__(self, baseMenor:int, baseMaior:int, altura:int, cor:str):
        self.baseMenor = baseMenor
        self.baseMaior = baseMaior
        self.altura = altura
        self.cor = cor

class Triangulo:
    def __init__(self,base:int, altura:int, cor:str):
        self.base = base
        self.altura = altura
        self.cor = cor