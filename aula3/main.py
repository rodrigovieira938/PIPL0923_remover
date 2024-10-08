from time  import sleep
import random
#tuples

tp1 = ("Rodrigo", "ATEC", 10793)
print(tp1)

print(tp1[0])
print(tp1[1])
print(tp1[2])

# print(tp1[3]) <- Erro

# tp1[0] = "Novo nome" <- Erro

list_temp = list(tp1)
print(list_temp)

list_temp[0] = "Novo nome"
tp1 = tuple(list_temp)

print(tp1)


print("--- unpack ---")

tp1 = ("Rodrigo", "ATEC", 10793)

(nome, escola, UFCD) = tp1

print(nome)
print(escola)
print(UFCD)

nome = "Novo nome 2"


nome = "Novo nome 2"
print("--- unpack list ---")
tp1 = ("Rodrigo", "ATEC", 10793)
temp_list = list(tp1)
print(type(temp_list))
(nome, escola, UFCD) = temp_list

print(nome)
print(escola)
print(UFCD)

print("--- metodos tuple ---")
tp1 = ("Rodrigo", "ATEC", 10793, "Rodrigo")
print(tp1.count("Rodrigo"))
# listas (arrays)

# listas (arrays)
print("--- listas (arrays) ---")

#lista vs array

my_list = ["Gonçalo", "Ana", "Rita", "Luiz"]

print(my_list)
print(my_list[0])
print(my_list[1])

my_list[0] = "Novo nome"

print(my_list[0])
print(my_list)

nomes = [    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia",    "Karla", "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro", "Quintino", "Rafael", "Sara", "Tatiana", "Ursula", "Vinicius", "Wagner", "Xavier", "Yasmin"]

print(nomes[0])
print(nomes[0:5]) # nomes[n:m] -> n a m -1

print(nomes[-10:-5])

print(nomes[0:20:3])

nomes.append("Rita")
print(nomes)

nomes.append("Aaron")
print(nomes[-1])

print("insert")
print(nomes[0:4])
print(f"{nomes.insert(1, "Novo nome")} ")
print(nomes[0:4])

print("remove")

nomes.remove("Novo nome")
print(nomes[0:4])

nomes[7]
print(nomes.pop(7))
print(nomes[7])

# print(nomes.remove("Outro nome")) <- Erro

# print(nomes.pop(70)) <- Erro

print("For array")

for nome in nomes:
    print(nome)

# receba 5 valores como input e adicione esses valores a uma lista
# mostre o conteudo de lista

arr = [
    input("Introduza o valor 1: "),
    input("Introduza o valor 2: "),
    input("Introduza o valor 3: "),
    input("Introduza o valor 4: "),
    input("Introduza o valor 5: "),
]
print(arr)

# receba N valores como input e adicione esses valores a uma lista
# mostre o conteudo da lista
# deve perguntar ao utilizador quantos valores pretende-se adicionar

arr = []

n = int(input("Quantos valores pretende adicionar: "))

for i in range(n):
    arr.append(input(f"Introduza o valor {i+1}: "))
print(arr)
# receba N notas (0 a 20) como input e adicione esses valores a uma lista
# mostre o conteuoda da lista
# deve perguntar ao utilizador quantos valores pretende adicionar
# deve garantir que todas as notas são validas
# deve assumir que o utilizador vai tentar adicionar valores numeros

num = int(input("Número de notas:"))
notas = []

for i in range(num):
    nota = float(input(f"Introduza a nota {i+1}: "))
    while not (0 <= nota <= 20):
        nota = float(input(f"Introduza a nota {i+1}: "))
        print(nota)
        if 20 >= nota >= 0:
            nota = nota
        else:
            print("Nota inválida. A nota tem que estar entre 0-20")
    notas.append(nota)
for n in notas:
    print(f"{n:.2f}")
# Faça um programa que leia 28 números inteiros e armazene-os em listas
# Armazene os núemros pares na lista PAR e os números IMPARES na lista impar

nums    = []
PAR   = []
IMPARES = []

for i in range(20):
    n = int(input(f"Introduza o {i+1}º número: "))
    nums.append(n)
    if n % 2 == 0:
        PAR.append(n)
    else:
        IMPARES.append(n)

print(f"Números {nums}")
print(f"Números pares: {PAR}")
print(f"Números impares: {IMPARES}")

# Set

mySet = {"val1", "val2", "val3", "val4"}
print(mySet)

"""
run 1: {"val2",'val1', 'val3','val4'}
run 1: {"val1",'val2', 'val4','val3'}
run 1: {"val1",'val2', 'val4','val3'}
run 1: {"val4",'val2', 'val1','val3'}
"""
for i in mySet:
    print(i)

print("----" * 3)

mySet = {"val1", "val2", "val3", "val4"}
print(mySet)

mySet.add("val15")
print(mySet)

mySet.add("val3")
print(mySet)

lista = list()

listNum = set()
for _ in range(1000):
    #sleep(0.01)
    i = random.randint(  0,  1000)
    listNum.add(i)
input("continuar? ")
print(listNum.len())


print("----" * 3)
print("----" * 3)

mySet = {"val1", "val2", "val3", "val4"}


print("val19" in mySet)
mySet.remove("val2")

print(mySet)

#mySet.remove("val2")

print("----" * 3)
print("----" * 3)


mySet = {"val1", "val2", "val3", "val4"}
mySet2 = {"val5", "val", "val3", "val4"}

#uniao

print("---" * 3,"union", "---" * 3)
resp = mySet.union(mySet2)
print(resp)

#interceção
print("---" * 3,"intercação", "---" * 3)
resp = mySet.intersection(mySet2)
print(resp)

#diferença
print("---" * 3,"diferença", "---" * 3)
resp = mySet.difference(mySet2)
print(resp)

resp = mySet2.difference(mySet)
print(resp)

#diferencia simetrica

resp = mySet.symmetric_difference(mySet2)
print(resp)
# dict