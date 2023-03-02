# Exercício 5.22
# a = int(input('Digite o primeiro número: '))
# b = int(input('Digite o segundo número: '))
# resultado = 0
# while True:
#     print('Escreva X na opção desejada, pressione ENTER para pular as opções indesejadas.')
#     adição = str(input('Adição: '))
#     if adição == 'X' or adição == 'x':
#         resultado = a + b
#         print(f'{a} + {b} = {resultado}')
#     subtração = str(input('Subtração: '))
#     if subtração == 'X' or subtração == 'x':
#         resultado = a - b
#         print(f'{a} - {b} = {resultado}')
#     divisão = str(input('Divisão: '))
#     if divisão == 'X' or divisão == 'x':
#         resultado = a / b
#         print(f'{a} / {b} = {resultado}')
#     multiplicação = str(input('Multpicação: '))
#     if multiplicação == 'X' or multiplicação == 'x':
#         resultado = a * b
#         print(f'{a} * {b} = {resultado}')
#     sair = str(input('Sair: '))
#     if sair == 'X' or sair == 'x':
#         break

# Exercício 5.23
# while True:
#     n = int(input('Número a ser testado: '))
#     if n < 2:
#         print(f'{n} não é um número primo')
#     else:
#         i = 2
#         primo = True
#         while i < n:
#             if n % i == 0:
#                 primo = False
#                 break
#             i += 1
#         if primo:
#             print(f'{n} é um número primo')
#         else:
#             print(f'{n} não é um número primo')
#     sair = str(input('Sair (s/n): '))
#     if sair == 's':
#         break

# Exercício 5.24
# while True:
# 	a = int(input('quantidade de números primos: '))
# 	y = 2
# 	contador = 0
# 	while True:
# 		x = 2
# 		primo = True
# 		while x < y:
# 			if y % x == 0:
# 				primo = False
# 			x += 1
# 		if primo == True:
# 			print(y)
# 			contador += 1
# 		if contador == a:
# 			break
# 		y += 1
# 	sair = str(input('Sair (s/n): '))
# 	if sair == 's':
# 		break

# Exercício 5.25

# Exercício 5.26
# while True:
#     print('Digite dois número para descobrir o resto da divisão entre eles.')
#     n = int(input('Digite o primeiro número: '))
#     a = n
#     m = int(input('Digite o segundo número: '))
#     b = m
#     acumulador = 0
#     resto = 0
#     while b <= a:
#         resto = a - b
#         acumulador += 1 
#         a -= b
#     print(acumulador)
#     print(a)
#     sair = str(input('Sair (s/n): '))
#     if sair.lower() == 's':
#         break

# Exercício 5.27
# while True:
#     n = int(input("Enter a number:"))
#     a = n
#     reverso = 0
#     while(n > 0):
#         dígito = n % 10
#         reverso = reverso * 10 + dígito
#         n //= 10
#     if(a == reverso):
#         print("The number is palindrome!")
#     else:
#         print("Not a palindrome!")
#     sair = str(input('Sair (s/n): '))
#     if sair.lower() == 's':
#         break