import math
print("1. Faça um Programa que peça dois números e imprima o maior deles.")
n1 = float(input("Introduza um número: "))
n2 = float(input("Introduza outro número: "))
if n1 > n2:
    print(n1)
else:
    print(n2)
print("2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.")
n1 = float(input("Introduza um número: "))
if n1 >= 0:
    print("Positivo")
else:
    print("Negativo")
print("3. Faça um Programa que verifique se uma letra digitada é \"F\" ou \"M\". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.")
sexo = input("Introduza o seu sexo (F - Feminino ou M - Masculino): ")
if sexo == "F" or sexo == "f":
    print("Feminino")
elif sexo == "M" or sexo == "m":
    print("Masculino")
else:
    print("Sexo inválido")
print("4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.")
letra = input("Introduza um caracter: ")
if len(letra) > 0:
    letra = letra[0] # ignorar mais caracteres se forem digitados
match letra:
    case 'a':
        print("A letra é uma vogal")
    case 'e':
        print("A letra é uma vogal")
    case 'i':
        print("A letra é uma vogal")
    case 'o':
        print("A letra é uma vogal")
    case 'u':
        print("A letra é uma vogal")
    case _:
        print("A letra é uma consoante")
print("5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:")
print("\t- A mensagem \"Aprovado\", se a média alcançada for maior ou igual a sete;")
print("\t- A mensagem \"Reprovado\", se a média for menor do que sete;")
print("\t- A mensagem \"Aprovado com Distinção\", se a média for igual a dez.")
n1 = int(input("Introduza a primeira nota"))
n2 = int(input("Introduza a segunda nota"))
media = (n1 + n2) / 2
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
print("6. Faça um Programa que leia três números e mostre o maior deles.")
nums = [
    float(input("Introduza o primeiro número: ")),
    float(input("Introduza o segundo número: ")),
    float(input("Introduza o terceiro número: "))
]
nums.sort() #ordena a lista em ordem crescente
print(nums[2])
print("7. Faça um Programa que leia três números e mostre o maior e o menor deles.")
nums = [
    float(input("Introduza o primeiro número: ")),
    float(input("Introduza o segundo número: ")),
    float(input("Introduza o terceiro número: "))
]
nums.sort() #ordena a lista em ordem crescente
print(nums[2])
print(nums[0])
print("8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.")
nums = [
    float(input("Introduza o primeiro preço: ")), #10 
    float(input("Introduza o segundo preço: ")),  # 8
    float(input("Introduza o terceiro preço: "))  # 9
]
if nums[0] < nums[1] and nums[0] < nums[2]:
    print("Deve comprar o primeiro produto")
elif nums[1] < nums[2] and nums[1] < nums[0]:
    print("Deve comprar o segundo produto")
elif nums[2] < nums[1] and nums[2] < nums[0]:
    print("Deve comprar o terceiro produto")
print("9. Faça um Programa que leia três números e mostre-os em ordem decrescente.")
nums = [
    float(input("Introduza o primeiro número: ")),
    float(input("Introduza o segundo número: ")),
    float(input("Introduza o terceiro número: "))
]
nums.sort(reverse=True)
print(nums)
print("10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem \"Bom Dia!\", \"Boa Tarde!\" ou \"Boa Noite!\" ou \"Valor Inválido!\", conforme o caso.")
turno = input("Digite o turno em que estudo (M-Matutino, V-Verpertino) our N-Noturno: ")
if   turno == "M" or turno == "M":
    print("Bom dia!")
elif turno == "V" or turno == "V":
    print("Boa Tarde!")
elif turno == "N" or turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
print("11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.")
print("\tFaça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:")
print("\t- salários até R$ 280,00 (incluindo) : aumento de 20%")
print("\t- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%")
print("\t- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%")
print("\t- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:")
print("\t\t# o salário antes do reajuste;")
print("\t\t# o percentual de aumento aplicado;")
print("\t\t# o valor do aumento;")
print("\t\t# o novo salário, após o aumento.")

salario = float(input("Introduza o salário: "))
if salario <= 280:
    aumento = 0.20
elif salario < 700:
    aumento = 0.15
elif salario < 1500:
    aumento = 0.10
else:
    aumento = 0.05
print(f"Salário antes do reajuste R$ {salario:.2f}")
print(f"O percentual de aumento aplicado {(aumento*100):.0f}%")
print(f"O valor do aumento R$ {(salario*aumento):.2f}")
print(f"Salário antes do reajuste R$ {(salario+salario*aumento):.2f}")

print("12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.")
print("\t- Desconto do IR:")
print("\t- Salário Bruto até 900 (inclusive) - isento")
print("\t- Salário Bruto até 1500 (inclusive) - desconto de 5%")
print("\t- Salário Bruto até 2500 (inclusive) - desconto de 10%")
print("\t- Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.")
valor_hora = float(input("Introduza o valor por hora: "))
quantidade_horas = float(input("Introduza a quantidade de horas trabalhadas: "))
salario_bruto = valor_hora * quantidade_horas
ir = 0
ir_perc = 0
if salario_bruto <= 900:
    ir_perc = 0
elif salario_bruto <= 1500:
    ir_perc = 0.05
elif salario_bruto <= 2500:
    ir_perc = 0.10
else:
    ir_perc = 0.20
ir = salario_bruto * ir_perc
inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11
salario_liquido = salario_bruto - ir - inss
print(f"Salário bruto: ({valor_hora} * {quantidade_horas}): R${salario_bruto}")
print(f"(-) IR ({(ir_perc*100):.0f}): R${ir}")
print(f"(-) INSS (10%): R${inss}")
print(f"FGTS (11%): R${fgts}")
print(f"Total de descontos: R${ir + inss}")
print(f"Salário Liquido: R${salario_liquido}")

print("13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.")
dia = input("Introduza o dia da semana (1-Domingo, 2-Segunda, ...): ")
match dia:
    case '1':
        print("Domingo")
    case '2':
        print("Segunda")
    case '3':
        print("Terça")
    case '4':
        print("Quarta")
    case '5':
        print("Quinta")
    case '6':
        print("Sexta")
    case '7':
        print("Sábado")
    case _:
        print("Valor inválido")
print("14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:")
print("\tMédia de Aproveitamento  Conceito")
print("\tEntre 9.0 e 10.0        A")
print("\tEntre 7.5 e 9.0         B")
print("\tEntre 6.0 e 7.5         C")
print("\tEntre 4.0 e 6.0         D")
print("\tEntre 4.0 e zero        E")
print("\tO algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.")
notas = [
    float(input("Introduza a primeira nota: ")),
    float(input("Introduza a segunda nota: "))
]
media = (notas[0] + notas[1]) / 2
if media > 9:
    letra = "A"
elif media > 7.5:
    letra = "B"
elif media > 6.0:
    letra = "C"
elif media > 4.0:
    letra = "D"
else:
    letra = "E"
if letra == "A" or letra == "B" or letra == "C":
    txt = "Aprovado"
else:
    txt = "Reprovado"
print(f"Nota  {notas}")
print(f"Média {media:.2f}")
print(f"{letra} ({txt})")

print("15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.")
print("\tDicas: ")
print("\t # Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;")
print("\t # Triângulo Equilátero: três lados iguais;")
print("\t # Triângulo Isósceles: quaisquer dois lados iguais;")
print("\t # Triângulo Escaleno: três lados diferentes;")

lado1 = int(input("Introduza o comprimento do primeiro lado: "))
lado2 = int(input("Introduza o comprimento do segundo lado: "))
lado3 = int(input("Introduza o comprimento do terceiro lado: "))

if lado1 == lado2 == lado3:
    print("Triângulo Equilátero")
if lado1 != lado2 != lado3:
    print("Triângulo Escaleno")
else:
    print("Triângulo Isósceles")

print("16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:")
print("\ta.Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;")
print("\tb.Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;")
print("\tc.Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;")
print("\td.Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;")
a = float(input("Introduza o valor de a: "))
b = float(input("Introduza o valor de b: "))
c = float(input("Introduza o valor de c: "))

if a == 0:
    print("a == 0, por isso não é uma equação de segundo grau")
else:
    delta = b**2-4*a*c
    print(f"Delta: {delta}")
    if delta < 0:
        print("delta é negativo não possuindo raizes")
    else:
        if delta == 0:
            print(f"A solução da equação é {-b/2*a}")
        else:
            sqrt = math.sqrt(delta)
            print(f"sqrt: {sqrt}")
            print(f"A solução da equação é {((-b+sqrt)/(2*a)):.4f} ou {((-b-sqrt)/(2*a)):.4f}")

print("17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.")
# https://pt.wikihow.com/Descobrir-se-um-Ano-%C3%A9-Bissexto
ano = int(input("Introduza um ano (ex: 2009): "))
bissexto = (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

if bissexto:
    print("Ano bissexto")
else:
    print("Ano não bissexto")

print("18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.")
data = input("Introduza uma data no formato dd/mm/aaaa: ")
if len(data) == 10:
    diasf = data[0].isnumeric() and data[1].isnumeric()
    mesf = data[3].isnumeric() and data[4].isnumeric()
    anof = data[6].isnumeric() and data[7].isnumeric() and data[8].isnumeric() and data[9].isnumeric()
    barras = data[2] == '/' and data[5] == "/"
    if diasf and mesf and anof and barras: # Formato está certo falta ver se o mês é menor our igal a 12 e se o dia está certo de acordo com o mês
        ano = int(data[6:10])
        ano_bissexto = (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0
        mes = int(data[3:5])
        dia = int(data[0:2])

        dias_dos_meses = [
            31,
            29 if ano_bissexto else 28,
            31,
            30,
            31,
            30,
            31,
            31,
            30,
            31,
            30,
            31
        ]
        if 0 < mes <= 12 and 0 < dia <= dias_dos_meses[mes]:
            print("Data válida")
        else:
            print("Data inválida")
    else:
        print("Data inválida")
else:
    print("Data inválida")