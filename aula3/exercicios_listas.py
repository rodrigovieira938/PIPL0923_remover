print("1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.")
arr = [
    int(input("Introduza o primeiro número: ")),
    int(input("Introduza o segundo número: ")),
    int(input("Introduza o terceiro número: ")),
    int(input("Introduza o quarto número: ")),
    int(input("Introduza o quinto número: ")),
]
print(arr)
print("2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.")
arr = []
for i in range(10):
    arr.append(float(input(f"Introduza o {i+1}º número: ")))
arr.sort(reverse=True)
print(arr)
print("3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.")
notas = []
for i in range(4):
    notas.append(float(input(f"Introduza o {i+1}ª nota: ")))
print(f"Notas: {notas}; Média: {sum(notas)/len(notas)}")
print("4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.")
caracteres = []
for i in range(10):
    caracteres.append(input(f"Introduza o {i+1}º caracter: "))
consoantes = [n for n in caracteres if not (n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u')] 
print(f"Consoantes {consoantes}; número de consoantes: {len(consoantes)}")
print("5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.")
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

print("6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.")

alunos = []

for x in range(10):
    aluno = []
    for y in range(4):
        aluno.append(float(input(f"Introduza a {y+1}ª nota do {x+1} aluno: ")))
    alunos.append(aluno)
medias = []

for aluno in alunos:
    medias.append(sum(aluno) / len(alunos))

for i in range(len(medias)):
    if medias[i] >= 7:
        print(f"O {i+1}º aluno tem uma média maior ou igual a 7 ({medias[i]})")
print("7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.")

arr = [
    int(input("Introduza o primeiro número: ")),
    int(input("Introduza o segundo número: ")),
    int(input("Introduza o terceiro número: ")),
    int(input("Introduza o quarto número: ")),
    int(input("Introduza o quinto número: ")),
]

print(f"Soma {sum(arr)}")
produto = 1
for i in arr:
    produto *= i
print(f"Multiplicação {produto}")

print("8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.")

idade  = []
altura = []

for x in range(5):
    idade.append(int(input(f"Introduza a idade do {x+1}º aluno: ")))
    altura.append(int(input(f"Introduza a altura em cm do {x+1}º aluno: ")))
idade.sort(reverse=True)
altura.sort(reverse=True)

print(f"Idades: {idade}")
print(f"Altura: {altura}")

print("9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.")

arr = []

for i in range(10):
    arr.append(int(input(f"Introduza o {i+1} número inteiro: ")))

soma = 0

for i in arr:
    soma += i**2
print(soma)

print("10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.")

arr1 = []
arr2 = []

for i in range(10):
    arr1.append(int(input(f"Introduza o {i+1} número inteiro do vetor 1: ")))
for i in range(10):
    arr2.append(int(input(f"Introduza o {i+1} número inteiro do vetor 2: ")))

arr3 = []

for i in range(20):
    if i % 2 == 0:
        arr3.append(arr1[(i+1) // 2])
    else:
        arr3.append(arr2[(i-1) // 2])
print(arr3)

print("11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.")

arr1 = []
arr2 = []
arr3 = []

for i in range(10):
    arr1.append(int(input(f"Introduza o {i+1} número inteiro do vetor 1: ")))
for i in range(10):
    arr2.append(int(input(f"Introduza o {i+1} número inteiro do vetor 2: ")))
for i in range(10):
    arr3.append(int(input(f"Introduza o {i+1} número inteiro do vetor 3: ")))


arr3 = []

for i in range(10):
    arr3.append(arr1[i])
    arr3.append(arr2[i])
    arr3.append(arr3[i])
print(arr3)

print("12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.")

idades = [
    8,
    20,
    49,
    29,
    71,
    71,
    2,
    28,
    100,
    27,
    88,
    76,
    14,
    48,
    42,
    49,
    50,
    75,
    8,
    87,
    8,
    16,
    86,
    54,
    9,
    26,
    57,
    1,
    16,
    71
]
alturas = [
    193,
    207,
    159,
    170,
    207,
    181,
    190,
    166,
    178,
    192,
    210,
    166,
    178,
    193,
    177,
    199,
    209,
    172,
    204,
    156,
    179,
    188,
    207,
    206,
    164,
    207,
    202,
    164,
    179,
    206
]

alunos_maior_treze_idx = [idx for idx in range(len(idades)) if idades[idx] > 13]
media_altura = 0
for aluno in alunos_maior_treze_idx:
    media_altura += alturas[aluno]
media_altura /= len(alunos_maior_treze_idx)
quantidade = 0
for aluno in alunos_maior_treze_idx:
    if alturas[aluno] < media_altura:
        quantidade += 1
print(f"Existe {quantidade} alunos com mais de 13 anos com altura inferior à média desses alunos")

print("13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).")
meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Agosto",
    "Novembro",
    "Dezembro"
]
media = 0
for i in range(12):
    media += float(input(f"Introduza a média da temperatura de {meses[i]}: "))
media /= 12
print(f"A média anual de temperatura é {media}")

print("14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:")
print("\ta. \"Telefonou para a vítima?\"")
print("\tb. \"Esteve no local do crime?\"")
print("\tc. \"Mora perto da vítima?\"")
print("\td. \"Devia para a vítima?\"")
print("\te. \"Já trabalhou com a vítima?\" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como \"Suspeita\", entre 3 e 4 como \"Cúmplice\" e 5 como \"Assassino\". Caso contrário, ele será classificado como \"Inocente\".")

respostas = []
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]
for i in range(len(perguntas)):
    resposta = ""
    while not(resposta == "s" or resposta == "S" or resposta == "n" or resposta == "N"):
        resposta = input(f"{perguntas[i]} Responda com [S]im ou [N]ão: ")
        if not(resposta == "s" or resposta == "S" or resposta == "n" or resposta == "N"):
            print("Reposta inválida")
    respostas.append(resposta.lower())
print(respostas)
respostas_com_sim = [n for n in respostas if n == "s"]

if len(respostas_com_sim) == 2:
    print("Suspeita")
elif 3 <= len(respostas_com_sim) <= 4:
    print("Cúmplice")
elif len(respostas_com_sim) == 5:
    print("Assassino")
else:
    print("Inocente")

print("15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:")

print("\ta. Mostre a quantidade de valores que foram lidos;")
print("\tb. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;")
print("\tc. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;")
print("\td. Calcule e mostre a soma dos valores;")
print("\te. Calcule e mostre a média dos valores;")
print("\tf. Calcule e mostre a quantidade de valores acima da média calculada;")
print("\tg. Calcule e mostre a quantidade de valores abaixo de sete;")
print("\th. Encerre o programa com uma mensagem;")

nums = []
num = 0
while num != -1:
    num = int(input("Introduza um número ou -1 para continuar: "))
    if num != -1:
        nums.append(num)
print(f"Foram lidos {len(nums)}")
print(f"Números {nums}")
nums.sort(reverse=True)
print(f"Números ao contrário {nums}")
soma = sum(nums)
print(f"A soma dos valores: {soma}")
media = soma / len(nums)
print(f"A média é {media}")
maior_da_media = 0
for num in nums:
    if num > media:
        maior_da_media += 1
print(f"Existe {maior_da_media} valores acima da média")

menor_que_7 = 0
for num in nums:
    if num < 7:
        menor_que_7 += 1

print(f"Existe {menor_que_7} valores menores que 7")

print("Programa encerrado")