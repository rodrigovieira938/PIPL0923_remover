# Crie um dicionario dinamico, onde pergunta ao utilizador quantos valores quer adicionar
# em seguida deve pedir o utilizador os dados es keus e valores que quer adicionar e adicionar os respetivos valores

n = int(input("Quantos valores quer adicionar: "))
dic = {}
for i in range(n):
    chave = input("Introduza a chave: ")
    dic[chave] = input("Introduza o valor: ")
print(dic)