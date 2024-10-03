import array

#Condições / Controlo de fluxo

#boolean

'''

T e T -> T
T e F -> F
F e T -> T
F e F -> F




T ou T -> T
T ou F -> T
F ou T -> T
F ou F -> F


T xou T -> F
T xou F -> T
F xou T -> T
F xou F -> F



'''

ano = 2024


#if (se)
if ano == 2024:
    print("ano = 2024")
else:
    print("Outro ano")

print("fora do if")

#Faça um programa que peça dois númros e imprima o maior deles
print("--"*10)
n1 = float(input("Introduza um número: "))
n2 = float(input("Introduza outro numero: "))

if n1 > n2:
    print(n1)
else:
    print(n2)
print("--"*10)

num = 5
# F ou T -> T
# num = 5
#      F         e      T
if num % 2 == 0 or num % 5 == 0:
    print("par or divisivel por 5")
else:
    print("impar e nao divisivel por 5")
'''
== <- comparações
=  <- atribuição
'''

#else if ( se não se )
if num % 2 == 0:
    print("par")
elif num % 5 == 0:
    print("div por 5")
else:
    print("impar ou nao div por 5")
#else ( se não)
#Faça um programa que verifique se um letra digitada é "F" ou "f" ou "M" ou "m".
# Conforme a letra escrever:
#    F - Feminino
#    M - Masculino
#    * -  Género inválido
gen = input("Indique o seu genero: ")
if gen == "F" or gen == "f":
    print("Feminino")
elif gen == "M" or gen == "m":
    print("Masculino")
else:
    print("Género inválido")
#switch ( escolha )
num = 10

match num:
    case 0:
        print("O numero é 0")
    case 1:
        print("O numero é 1")
    case 5:
        print("O numero é 5")
    case _:
        print("Outro valor")
memu = """------ Menu -------
- op1 ......... 1 -
- op2 ......... 2 - 
- op3 ......... 3 -
-------------------
"""

print(memu)
op = input("Selecione a op: ")
match op:
    case "1":
        print("op 1")
    case "2":
        print("op 2")
    case "3":
        print("op 3")
    case _:
        print("Outro valor")

#loops

#while ( enquanto - faça)

count = 0
while op != "q":
    print(f"loop: {count}")
    op = input("Selecione a op: ")
    count += 1
num = 0
while num < 10:
    print("num")
    num += 1
'''
    num += 1
    num = num + 1
    
    num += 4
    num = num + 4

    num *= 3
    num = num * 3
'''
# Range

range(0,10,2)

"""
range(a,b,c)

a - LB(Lower bound), se oculto = 0

b - UB(Upper bound)[

c - step, se oculto c = 1

range(1,5)
1,2,3,4,

range(0,5)
0, 1, 2, 3, 4

range(0, 10, 2)
0, 2, 4, 6, 8

"""
#for (par)

print("---" * 10)
for elm in range(0, 11, 2):
    print(elm)

print("---" * 10)
for elm in range(0, 100):
    if elm % 2 == 0:
        continue
    print(elm)
    #if elm == 50:
    #    break
print("---" * 10)
print("---" * 10)

nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia",    "Karla", "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro", "Quintino", "Rafael", "Sara", "Tatiana", 
         "Ursula", "Vinicius", "Wagner", "Xavier", "Yasmin"]

for nome in nomes:
    print(nome)

print("Fim do loop")


print(nome.count("Daniela"))

print(nomes.__len__())
print(len(nomes))

print(nomes.__contains__("Sara"))
print(nomes.__contains__("Ana"))
print("Pedro" in nomes)

#nomes.sort(reverse=True)

print("------"*5)
nomes.sort()
print(nomes)

"""

var
tipos de dados
type cast - int("..."), str(...)
tuplos
op com var
if
elif
else
and / or
match
while
for
list
"""

"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""
nota = input("Introduza uma nota entre 0-10: ")
condicao = nota.isdigit()
while not (condicao and int(nota) >= 0 and int(nota) <= 10):
    print("Nota Inválida")
    nota = input("Introduza uma nota entre 0-10: ")