class Morada:
    def __init__(self):
        self.morada = "Morada"
    def __str__(self):
        return self.morada

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __repr__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"
