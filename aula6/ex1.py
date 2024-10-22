"""
Crie uma app que peça ao utilizador os sesus dados e guarde esses 
dados num ficheiro de texto

deve utilizar o try/except para evitar erros

"""

nome = input("Introduza o seu nome: ")
idade = None
while idade == None:
    try:
        idade = int(input("Introduza a sua idade: "))
    except:
        print("Tem que introduzir um número para a sua idade!")
email = input("Introduza o seu email: ")

ficheiro = open("informacoes.txt", "wt")
ficheiro.write("{\n")
ficheiro.write(f"\t\"nome\": \"{nome}\",\n")
ficheiro.write(f"\t\"idade\": {idade},\n")
ficheiro.write(f"\t\"email\": \"{email}\"\n")
ficheiro.write("}")
ficheiro.close()