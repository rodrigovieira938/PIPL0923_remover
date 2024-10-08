nomes = [    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia",    "Karla", "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro", "Quintino", "Rafael", "Sara", "Tatiana",    "Ursula", "Vinicius", "Wagner", "Xavier", "Yasmin"]

# lista de nomes que terminam com "a"

lista2 = []

for nome in nomes:
    if nome[-1] == "a":
        lista2.append(nome)
print(f"Lista 2:{lista2} ")
lista3 = [n for n in lista2 if n[-1] == "a"]

print(f"Lista 3:{lista3} ")

lista3 = [n.__len__() for n in lista2 if n[-1] == "a"]

print(f"Lista 3:{lista3} ")

print("---")

lista3 = [n for n in nomes if n.lower().count("t") >= 1]

print(f"Lista 3: {lista3}")

print("---")

lista3 = []
for nome in nomes:
    if "r" in nome:
        lista3.append(nome)

print(f"Lista 3: {lista3}")

lista3 = [n for n in nomes if n.lower().count("r") > 0]

print(f"Lista 3: {lista3}")

lista3 = [n for n in nomes if 'r' in n]

print(f"Lista 3: {lista3}")


print("---------")
print("---------")

nomes.sort(reverse=True)

print(nome)

nomes2 = nomes

print(nomes2[0])
print(nomes[0])

nomes2[0] = "Novo nome"

print(nomes2[0])
print(nomes[0])


print("---------")
print("---------")

copy_nome = nomes.copy()

print(copy_nome[0])
print(nomes[0])

copy_nome = "foo"

print(copy_nome[0])
print(nomes[0])

print("---------")
print("---------")

nova_list2 = [nome for nome in nomes]

print(nova_list2[0])
print(nomes[0])

nova_list2[0] = "Marco"

print(nova_list2[0])
print(nomes[0])