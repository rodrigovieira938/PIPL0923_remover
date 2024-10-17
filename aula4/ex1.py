"""
1 - Crie um dicionario com os seus dados: nome e  turma
2 - Usando o dicionário criado anteriormente, imprima seu nome
3 - Adiciona a sua localidade
4 - Mostre a msg:
"Olá, o meu nome é <Nome>, sou de <Localidade> e estou na turma <Turma>"
"""

dados = {
    "Nome":"Rodrigo Vieira",
    "Turma":"PIPL0923",
}

print(dados["Nome"])

dados["Localidade"] = "Azeitão"

print(f"Olá, o meu nome é {dados["Nome"]}, sou de {dados['Localidade']} e estou na turma {dados['Turma']}")