import math

print("1. Faça um Programa que mostre a mensagem \"Alo mundo\" na tela\n\tAlo Mundo")
print ("Alô Mundo")
print("2. Faça um Programa que peça um número e então mostre a mensagem \"O número informado foi [número]\"")
n = input("Introduza um número: ")
print(f"O número informado foi {n}" )
print("3. Faça um Programa que peça dois números e imprima a soma.")
n1 = int(input("Introduza um número: "))
n2 = int(input("Introduza outro número: "))
print ("Soma: ", n1+n2)
print("4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.")
n1 = float(input("Introduza a primeira nota: "))
n2 = float(input("Introduza a segunda nota: "))
n3 = float(input("Introduza a terceira nota: "))
n4 = float(input("Introduza a quarta nota: "))
m = (n1+n2+n3+n4)/4
print ("Media: ", m)
print("5. Faça um Programa que converta metros para centímetros.")
m = float(input("Metros: "))
print (f"Centímetros: {(m * 100):.2f} cm")
print("6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.")
r = float(input("Raio do círculo: "))
area = 3.14 * (r ** 2)
print (f"Área do círculo: {area}")
print("7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.")
l = float(input("Lado do quadrado em m: "))
area = l * l
print (f"Dobro da area do quadrado: {(area*2):.2f} m²")
print("8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.")
sm = float(input("Sálario por hora: "))
nh = int(input("Horas trabalhadas no mês: "))
salario = sm * nh
print(f"Salario: R$ {salario}")
print("9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.\n\tC = 5 * ((F-32) / 9).")
tf = float(input("Temperatura em Fahrenheit: "))
print (f"Temperatura em Celsius: {(5/9 * (tf-32)):.2f}")
print("10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.")
tc = float(input("Temperatura em Celsius: "))
print (f"Temperatura em Fahrenheit: {(9*tc/5 + 32):.2f}")
print("11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:\n\ta. o produto do dobro do primeiro com metade do segundo.\n\tb. a soma do triplo do primeiro com o terceiro.\n\tb. o terceiro elevado ao cubo.")
n1 = int(input("Introduza o primeiro número inteiro: "))
n2 = int(input("Introduza o segundo número inteiro: "))
n3 = float(input("Número real: "))

print ("Soma:", ((2*n1) * (n2/2)))
print ("Produto:", (3 * n1) + n3)
print ("Cubo:", n3**3)
print("12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:\n\t(72.7*altura) - 58")
altura = float(input("Altura:"))
print ("Peso ideal:", (72.7*altura) - 58)
print("13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:\n\ta. Para homens: (72.7*h) - 58\n\tb. Para mulheres: (62.1*h) - 44.7")
sexo = int(input("Escolha: 1- Sexo Masculino / 2- Sexo Feminino: "))
h = float(input("Altura:"))
peso = float(input("Peso:"))

peso_ideal = (72.7*h) - 58 if sexo == 1 else (62.1*h) - 44.7

if peso < peso_ideal:
	print("Abaixo do peso ideal!")
elif peso == peso_ideal:
	print("Dentro do peso ideal!")
else:
	print("Acima do peso ideal!")
print (f"Peso: {peso:.2f} / Peso ideal: {peso_ideal:.2f}")
print("14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.")
peso = float(input("Peso:"))
if peso > 50:
	excedente = peso - 50
	multa = excedente * 4
else:
	excedente = 0
	multa = 0
print ("Peso: {peso:.2f} Kg")
print ("Excesso: {excedente:.2f} Kg")
print ("Multa: R$ {multa:.2f}")
print("15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:")
print("\ta. salário bruto.\n\tb. quanto pagou ao INSS.\n\tc. quanto pagou ao sindicato.\n\td. o salário líquido.\n\te. calcule os descontos e o salário líquido, conforme a tabela abaixo:")
print("\t + Salário Bruto : R$\n\t - IR (11%) : R$\n\t - INSS (8%) : R$\n\t - Sindicato ( 5%) : R$\n\t = Salário Liquido : R$")
print("\tObs.: Salário Bruto - Descontos = Salário Líquido.")
vh = float(input("Valor da hora:"))
qh = int(input("Quantidade de horas trabalhadas:"))

salario_bruto = vh * qh
inss = 8/100 * salario_bruto
sindicato = 5/100 * salario_bruto
ir = 11/100 * salario_bruto

salario_liquido = salario_bruto - inss - sindicato - ir

print (" + Salário Bruto: R$ {salario_bruto:.2f}")
print (" - IR: R$ {ir:.2f}")
print (" - INSS: R$ {inss:.2f}")
print (" - Sindicato: R$ {sindicato:.2f}")
print (" = Salário Liquido: R$ {salario_liquido:.2f}")

print("16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.")
tamanho = float(input("Tamanho em metro quadrados: "))
litros_necessario = tamanho / 3
latas_necessarias = math.ceil(litros_necessario / 18)
print(f"Latas necessárias: {latas_necessarias}")
print(f"Preço total: R$ {latas_necessarias*80.0}")