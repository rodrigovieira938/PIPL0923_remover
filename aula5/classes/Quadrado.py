"""
Quadrado
    lado: int
    cor: str

"""


class Quadrado:
    def __init__(self, lado: int, cor: str):
        self.lado = lado
        self.cor = cor
    
    def area(self) -> int:
        # return self.lado * self.lado
        # return pow(self.lado, 2)
        return self.lado**2
    
    def perimetro(self) -> int:
        return self.lado*4
    
    def mudar_cor(self, cor: str):
        self.cor = cor

    def infos(self) -> str:
        return f""