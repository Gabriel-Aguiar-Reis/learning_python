#Exercício 5.11
# depósito = float(input('Digite o valor do depósito: '))
# taxa = float(input('Digite o valor da taxa de juros anual: '))
# n = 1
# valor_acumulado = depósito
# while n <= 24:
#     valor_acumulado = valor_acumulado + valor_acumulado * ((taxa/100)/12)
#     print(f'{valor_acumulado:6.2f}')
#     n = n + 1
# print(f'O valor final é: {valor_acumulado:6.2f}')

#Exercício 5.12
# depósito_inicial = float(input('Digite o valor do depósito: '))
# taxa = float(input('Digite o valor da taxa de juros anual: '))
# depósito_mensal = float(input('Digite o valor do aporte mensal: '))
# n = 1
# valor_acumulado = depósito_inicial
# while n <= 24:
#     valor_acumulado = valor_acumulado + depósito_mensal  + valor_acumulado * ((taxa/100)/12)
#     print(f'{valor_acumulado:6.2f}')
#     n = n + 1
# print(f'O valor final é: {valor_acumulado:6.2f}')

#Exercício 5.13
# dívida = float(input('Digite o valor da dívida: '))
# taxa = float(input('Digite o valor da taxa de juros mensal: '))
# depósito_mensal = float(input('Digite o valor do aporte mensal: '))
# valor_acumulado = dívida
# número_meses = 0
# total_pago = 0
# total_juros = 0
# while valor_acumulado > 0:
#     número_meses = número_meses + 1
#     valor_acumulado = valor_acumulado - depósito_mensal  + valor_acumulado * (taxa/100)
#     total_pago = total_pago + depósito_mensal
#     if valor_acumulado < 0:
#         total_pago = total_pago + valor_acumulado
# total_juros = total_pago - dívida
# print(f'O número de meses é {número_meses}')
# print(f'O valor pago é {total_pago:.2f} e o valor dos respectivos juros é {total_juros:.2f}')

#Exercício 5.14
# soma = 0
# números_somados = 0
# while True:
# 	variable = int(input('digite um número a somar ou 0 para sair: '))
# 	soma += variable
# 	números_somados += 1
# 	média = soma / números_somados
# 	if variable == 0:
# 		break
# print(f'soma: {soma}')
# print(f'números somados: {números_somados}')
# print(f'média: {média}')

#Exercício 5.15
# soma = 0
# while True:
# 	cod = int(input('digite o código do produto ou 0 para encerrar: '))
# 	if cod == 0:
# 		break
# 	elif cod == 1:
# 		qnt = int(input('digite a quantidade: '))
# 		soma = soma + qnt * 0.5
# 	elif cod == 2:
# 		qnt = int(input('digite a quantidade: '))
# 		soma = soma + qnt * 1
# 	elif cod == 3:
# 		qnt = int(input('digite a quantidade: '))
# 		soma = soma + qnt * 4
# 	elif cod == 5:
# 		qnt = int(input('digite a quantidade: '))
# 		soma = soma + qnt * 7
# 	elif cod == 9:
# 		qnt = int(input('digite a quantidade: '))
# 		soma = soma + qnt * 8
# 	else:
# 		print('Código Inválido')
# print(f'O total de compras é R$ {soma}')

# Exercício 5.18
# valor = float(input('Digite o valor a pagar: '))
# cédulas = 0
# atual = 100
# a_pagar = valor
# while True:
# 	if atual <= a_pagar:
# 		a_pagar -= atual
# 		cédulas += 1
# 	else:
# 		print(f'{cédulas} cédula(s) de R$ {atual}')
# 		if a_pagar == 0:
# 			break
# 		if atual == 100:
# 			atual = 50
# 		elif atual == 50:
# 			atual = 20
# 		elif atual == 20:
# 			atual = 10
# 		elif atual == 10:
# 			atual = 5
# 		elif atual == 5:
# 			atual = 1
# 		elif atual == 1:
# 			break
# 		cédulas = 0

# Exercício 5.19
# valor = float(input('Digite o valor a pagar: '))
# cédulas = 0
# atual = 100
# a_pagar = valor
# while True:
# 	if atual <= a_pagar:
# 		a_pagar -= atual
# 		cédulas += 1
# 	else:
# 		print(f'{cédulas} cédula(s) de R$ {atual}')
# 		if a_pagar == 0:
# 			break
# 		if atual == 100:
# 			atual = 50
# 		elif atual == 50:
# 			atual = 20
# 		elif atual == 20:
# 			atual = 10
# 		elif atual == 10:
# 			atual = 5
# 		elif atual == 5:
# 			atual = 1
# 		elif atual == 1:
# 			atual = 0.5
# 		elif atual == 0.5:
# 			atual = 0.25
# 		elif atual == 0.25:
# 			atual = 0.10	
# 		elif atual == 0.10:
# 			atual = 0.05
# 		elif atual == 0.05:
# 			break
# 		cédulas = 0