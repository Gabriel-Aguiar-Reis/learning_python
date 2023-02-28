# ### concatenação e composição

# # a='casa'
# # print(a+'mento')

# ## %d = números inteiros
# ## %s = strings
# ## %f = números decimais

# # nome='João'
# # dinheiro=33.2
# # idade=19
# # print('%s, de %d anos tem %5.2f reais em seu bolso' % (nome, idade , dinheiro))

# # print('{}, de {} anos tem {:5.2f} reais em seu bolso'.format(nome, idade, dinheiro))

# ## f-string

# # print(f'{nome}, de {idade} anos tem {dinheiro:5.2f} reais em seu bolso')

# ### fataimento de string

# # s='gabriel'
# # print(s[0:2])
# # print(s[:])

# ### sequências e tempo

# # dívida=0
# # compra=100
# # dívida=dívida+compra
# # compra=200
# # dívida=dívida+compra
# # compra=300
# # dívida=dívida+compra
# # compra=0
# # print(dívida)

# ### rastreamento
# ### entrada de dados

# # x=input('Digite um número: ')
# # print(x)
# # nome=input('Digite seu nome: ')
# # print(f'Você digitou {nome}')
# # print(f'Bem-vindo {nome}')

# ### conversão de entrada de dados

# ## função int para converter para números inteiros
# ## função float para converter para números decimais

# # anos=int(input('Anos de serviço: '))
# # valor_anual=float(input('Valor por ano: '))
# # bônus=anos*valor_anual
# # print(f'Bônus de R$ {bônus:5.2f}')

# ## exercícios

# # n1=int(input('Primeiro Número: '))
# # n2=int(input('Segundo Número: '))
# # soma=n1+n2
# # print(f'O valor da soma é {soma}')

# # metros=float(input('metros = '))
# # centímetros=int(metros*100)
# # print(f'Isso equivale a {centímetros} centímetros')

# # dias=int(input('dias = '))
# # horas=int(input('horas = '))
# # minutos=int(input('minutos = '))
# # segundos=int(input('segundos = '))
# # soma=segundos+minutos*60+horas*60*60+dias*24*60*60
# # print(f'Isso equivale a {soma} segundos')

# # salário=float(input('Salário = '))
# # aumento=int(input('aumento = '))
# # valor_aumento=salário*aumento/100
# # valor_final=salário+valor_aumento
# # print(f'O valor de aumento é R$ {valor_aumento:.2f} e o valor final R$ {valor_final:.2f}')

# # tempC=int(input('temperatura = '))
# # tempF=(tempC*9/5)+32
# # print(f'a temperatura é {tempF:.0f}ºF')

# #### CAPÍTUlO 4 - CONDIÇÕES

# ### IF

# # a=int(input('first value: '))
# # b=int(input('second value: '))
# # if a>b:
# #     print('first value is bigger')
# # if b>a:
# #     print('second value is bigger')

# # age=int(input('age of your car: '))
# # if age<=3:
# #     print("it's a fresh car")
# # if age>3:
# #     print("it's a old car")

# # speed=int(input("what's your car speed: "))
# # if speed>80:
# #     valor_multa=(speed-80)*5
# #     print(f"now, you've to pay a traffic ticket of {valor_multa} bucks, idiot")
# # if speed<=80:
# #     print('okay, you can go now')

# # salário=float(input("write your wage to calculate the income tax: "))
# # base=salário
# # imposto=0
# # if base>3000:
# #     imposto=imposto+((base-3000)*0.35)
# #     base=3000
# # if base>1000:
# #     imposto=imposto+((base-1000)*0.20)
# # print(f'wage = ${salário:6.2f} income tax = ${imposto:6.2f}')

# ## Exercícios

# # a=int(input(" write the first number: "))
# # b=int(input(" write the second number: "))
# # c=int(input(" write the third number: "))
# # if a>b and a>c:
# #     print(f"{a} is the big one")
# # if b>a and b>c:
# #     print(f"{b} is the big one") 
# # if c>a and c>b:
# #     print(f"{c} is the big one")

# ## eu adicionei 'and' mesmo sem ter aprendido ainda

# # wage=int(input("wage = "))
# # base=wage
# # wage_increase=0
# # if base>1250:
# #     wage_increase=wage_increase+base*0.1
# # if base<=1250:
# #     wage_increase=wage_increase+base*0.15
# # print(f'{wage_increase} is the increase value')

# ### ELSE

# # age=int(input('age of your car: '))
# # if age<=3:
# #     print("it's a fresh car")
# # else:
# #     print("it's a old car")

# # distance=float(input("what distance do you wanna travel, in km? "))
# # base=distance
# # travel_value=0
# # if base>200:
# #     travel_value=travel_value+(base-200)*0.45
# #     base=200
# # if base<=200:
# #     travel_value=travel_value+base*0.5
# # print(f"the travel's value is $ {travel_value:5.2f}")

# ### ESTRUTURAS ANINHADAS

# ### ELIF

# # categoria=int(input('digite a categoria do produto: '))
# # if categoria==1:
# #     preço=10
# # elif categoria==2:
# #     preço=18
# # elif categoria==3:
# #     preço=23
# # elif categoria==4:
# #     preço=26
# # elif categoria==5:
# #     preço=31
# # else:
# #     print('categoria inválida, digite um valor entre 1 e 5!')
# #     preço=0
# # print(f"o preço do produto é: R${preço:6.2f}")

# ## exercícios

# # a=float(input('primeiro número: '))
# # operação=str(input('operação desejada (+,*,/,-): '))
# # b=float(input('segundo número: '))
# # resultado=0
# # if operação=='+':
# #     resultado=a+b
# # elif operação=='-':
# #     resultado=a-b
# # elif operação=='/':
# #     resultado=a/b
# # elif operação=='*':
# #     resultado=a*b
# # else:
# #     print('o valor preenchido é inválido')
# #     resultado=0
# # print(f'seu resultado é {resultado:.3f}')

# # house_value=float(input('house value: '))
# # wage=float(input('your wage: '))
# # amount_of_years=int(input('amount of paying years: '))
# # monthly_installment_value=house_value/(amount_of_years*12)
# # if monthly_installment_value<=(wage*0.3):
# #     print('the bank loan was successful')
# #     print(f'the montlhy amount to be paid is ${monthly_installment_value:.2f}')
# # else:
# #     print('the bank loan has been denied')

# # khw=float(input('KWh cosumidos: '))
# # tipo=str(input('tipo de instalação (R, C ou I): '))
# # preço=0
# # if tipo=='R' and khw<=500:
# #     preço=0.4*khw
# # elif tipo=='R' and khw>500:
# #     preço=0.65*khw
# # elif tipo=='C' and khw<=1000:
# #     preço=0.55*khw
# # elif tipo=='C' and khw>1000:
# #     preço=0.6*khw
# # elif tipo=='I' and khw<=5000:
# #     preço=0.55*khw
# # elif tipo=='I' and khw>5000:
# #     preço=0.6*khw
# # print(f'valor a pagar R${preço:5.2f}')

# #### CAPÍTULO 5 - REPETIÇÕES

# # x=1
# # while x<=3:
# #     print(x)
# #     x=x+1

# ### Exercícios

# # x=10
# # while x>=0:
# #     print(x)
# #     x=x-1
# # else:
# #     print('FOGO!')

# ### CONTADORES

# # fim = int(input('último número a imprimir: '))
# # x=0
# # while x <= fim:
# #     if x % 2 == 0:
# #         print(x)
# #     x = x + 1

# # fim = int(input('último número a imprimir: '))
# # x=0
# # while x <= fim:
# #     print(x)
# #     x = x + 2

# ### Exercícios

# # fim = int(input('último número a imprimir: '))
# # x=0
# # while x <= fim:
# #     if x % 2 != 0:
# #         print(x)
# #     x = x + 1

# # fim = int(input('último número a imprimir: '))
# # x=0
# # while x <= 30:
# #     if x % 3 == 0 and x != 0:
# #         print(x)
# #     x = x + 1

# # n = int(input('Tabuada de (adição): '))
# # x = 1
# # while x <= 10:
# #     print(n + x)
# #     x = x + 1

# ### Excercícios

# # n = int(input('Tabuada de (adição): '))
# # x = 1
# # while x <= 10:
# #     print(n * x)
# #     x = x + 1

# # n = int(input('Tabuada de: '))
# # x = int(input('Início da tabuada: '))
# # y = int(input('Fim da tabuada: '))
# # z = x
# # while z <= y:
# #     print(n * z)
# #     z = z + 1

# # a = int(input('primeiro número: '))
# # b = int(input('segundo número: '))
# # x = a
# # y = b
# # resultado = 0
# # while y > 0:
# #     resultado = resultado + x
# #     y = y - 1
# # print(f'{a}*{b}')
# # print(f'O resultado é {resultado}')

# # a = int(input('primeiro número: '))
# # b = int(input('segundo número: '))
# # x = a
# # y = b
# # resultado_inteiro = 0
# # resto = 0
# # multiplicação = 0
# # while y < x:
# #     resultado_inteiro = resultado_inteiro + 1
# #     y = y + b 
# # if y >= x:
# #     while y > b:
# #         multiplicação = multiplicação + b 
# #         resto = x - multiplicação 
# #         y = y - b
# # print(f'{a}/{b}')
# # print(f'O resultado é {resultado_inteiro}, e o resto é {resto}.')

# # pontos = 0
# # questão = 1
# # while questão <= 3:
# #     resposta = input(f'resposta da questão {questão}: ')
# #     if questão == 1 and (resposta == 'b' or resposta == 'B'):
# #         pontos = pontos + 1
# #     if questão == 2 and (resposta == 'a' or resposta == 'A'):
# #         pontos = pontos + 1
# #     if questão == 3 and (resposta == 'd' or resposta == 'D'):
# #         pontos = pontos + 1
# #     questão = questão + 1
# # print(f'O aluno fez {pontos} ponto(s)')

# ### ACUMULADORES

# # n = 1
# # soma = 0
# # while n <= 10:
# #     x = int(input(f'Digite o {n}º número: '))
# #     soma = soma + x
# #     n = n + 1
# # print(f'Soma: {soma}')

# # x = 1
# # soma = 0
# # while x <= 5:
# #     n = int(input(f'Digite o {x}º número: '))
# #     soma = soma + n
# #     x = x + 1
# # print(f'Média: {soma/5:5.2f}')

# ### Exercícios

# # depósito = float(input('Digite o valor do depósito: '))
# # taxa = float(input('Digite o valor da taxa de juros anual: '))
# # n = 1
# # valor_acumulado = depósito
# # while n <= 24:
# #     valor_acumulado = valor_acumulado + valor_acumulado * ((taxa/100)/12)
# #     print(f'{valor_acumulado:6.2f}')
# #     n = n + 1
# # print(f'O valor final é: {valor_acumulado:6.2f}')

# # depósito_inicial = float(input('Digite o valor do depósito: '))
# # taxa = float(input('Digite o valor da taxa de juros anual: '))
# # depósito_mensal = float(input('Digite o valor do aporte mensal: '))
# # n = 1
# # valor_acumulado = depósito_inicial
# # while n <= 24:
# #     valor_acumulado = valor_acumulado + depósito_mensal  + valor_acumulado * ((taxa/100)/12)
# #     print(f'{valor_acumulado:6.2f}')
# #     n = n + 1
# # print(f'O valor final é: {valor_acumulado:6.2f}')

# # dívida = float(input('Digite o valor da dívida: '))
# # taxa = float(input('Digite o valor da taxa de juros mensal: '))
# # depósito_mensal = float(input('Digite o valor do aporte mensal: '))
# # valor_acumulado = dívida
# # número_meses = 0
# # total_pago = 0
# # total_juros = 0
# # while valor_acumulado > 0:
# #     número_meses = número_meses + 1
# #     valor_acumulado = valor_acumulado - depósito_mensal  + valor_acumulado * (taxa/100)
# #     total_pago = total_pago + depósito_mensal
# #     if valor_acumulado < 0:
# #         total_pago = total_pago + valor_acumulado
# # total_juros = total_pago - dívida
# # print(f'O número de meses é {número_meses}')
# # print(f'O valor pago é {total_pago:.2f} e o valor dos respectivos juros é {total_juros:.2f}')

# ### OPERADORES DE ATRIBUIÇÃO ESPECIAIS

# # x += 1 >> x = x + 1
# # y -= 1 >> y = y - 1
# # c *= 2 >> c = c * 2 
# # d /= 2 >> d = d / 2
# # e **= 2 >> e = e ** 2
# # f //= 4 >> f = f // 4

# ### INTERROMPENDO A REPETIÇÃO

# # s = 0
# # while True:
# # 	v = int(input('digite um número a somar ou 0 para sair: '))
# # 	if v == 0:
# # 		break
# # 	s += v
# # print(s)

# ### EXERCÍCIOS

# # soma = 0
# # números_somados = 0
# # while True:
# # 	variable = int(input('digite um número a somar ou 0 para sair: '))
# # 	soma += variable
# # 	números_somados += 1
# # 	média = soma / números_somados
# # 	if variable == 0:
# # 		break
# # print(f'soma: {soma}')
# # print(f'números somados: {números_somados}')
# # print(f'média: {média}')

# # soma = 0
# # while True:
# # 	cod = int(input('digite o código do produto ou 0 para encerrar: '))
# # 	if cod == 0:
# # 		break
# # 	elif cod == 1:
# # 		qnt = int(input('digite a quantidade: '))
# # 		soma = soma + qnt * 0.5
# # 	elif cod == 2:
# # 		qnt = int(input('digite a quantidade: '))
# # 		soma = soma + qnt * 1
# # 	elif cod == 3:
# # 		qnt = int(input('digite a quantidade: '))
# # 		soma = soma + qnt * 4
# # 	elif cod == 5:
# # 		qnt = int(input('digite a quantidade: '))
# # 		soma = soma + qnt * 7
# # 	elif cod == 9:
# # 		qnt = int(input('digite a quantidade: '))
# # 		soma = soma + qnt * 8
# # 	else:
# # 		print('Código Inválido')
# # print(f'O total de compras é R$ {soma}')

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

# ### REPETIÇÕES ANINHADAS

# # tabuada = 1
# # while tabuada <= 10:
# # 	número = 1
# # 	while número <= 10:
# # 		print(f'{tabuada} x {número} = {tabuada * número}')
# # 		número += 1
# # 	tabuada += 1

# ### EXERCÍCIOS

# while True:
# 	valor = float(input('Digite o valor a pagar ou 0 para encerrar: '))
# 	cédulas = 0
# 	atual = 100
# 	a_pagar = valor
# 	while True:
# 		if atual <= a_pagar:
# 			a_pagar -= atual
# 			cédulas += 1
# 		else:
# 			print(f'{cédulas} cédula(s) de R$ {atual}')
# 			if a_pagar == 0:
# 				break
# 			if atual == 100:
# 				atual = 50
# 			elif atual == 50:
# 				atual = 20
# 			elif atual == 20:
# 				atual = 10
# 			elif atual == 10:
# 				atual = 5
# 			elif atual == 5:
# 				atual = 1
# 			elif atual == 1:
# 				atual = 0.5
# 			elif atual == 0.5:
# 				atual = 0.25
# 			elif atual == 0.25:
# 				atual = 0.10	
# 			elif atual == 0.10:
# 				atual = 0.05
# 			elif atual == 0.05:
# 				break
# 			cédulas = 0
# 	if valor == 0:
# 		break

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

### F-STRINGS

#### CAPÍTULO 6 - LISTAS, DICIONÁRIOS, TUPLAS E CONJUNTOS

# notas = [0, 0, 0, 0, 0, 0, 0]
# soma = 0
# x = 0
# while x < 7:
#     notas[x] = float(input(f'Nota {x + 1}: '))
#     soma += notas [x]
#     x += 1
# x = 0
# while x < 7:
#     print(f'Nota {x + 1}: {notas [x]:6.2f}')
#     x += 1
# print(f'Média: {soma / x:5.2f}')

### Trabalhando com Índices
### Cópia e fatiamento de listas
### Tamanho de listas
### Adiçao de elementos

# listA = []
# listB = []
# listC = []
# x = 0
# while True:
#     x = str(input('Insira o valor a ser adicionado na primeira lista, digite "s" para sair: '))
#     if x == "s":
#         break
#     else:
#         listA.append(x)
# x = 0
# while True:
#     x = str(input('Insira o valor a ser adicionado na segunda lista, digite "s" para sair: '))
#     if x == "s":
#         break
#     else:
#         listB.append(x)
# listC.extend (listA + listB)
# if listC == []:
#     print('Não há valores informados')
# else:
#     print(f'Os valores unificados das duas listas são: {listC}')

# listA = []
# listB = []
# listC = []
# x = 0
# while True:
#     x = str(input('Insira o valor a ser adicionado na primeira lista, digite "s" para sair: '))
#     if x == "s":
#         break
#     else:
#         listA.append(x)
# x = 0
# while True:
#     x = str(input('Insira o valor a ser adicionado na segunda lista, digite "s" para sair: '))
#     if x == "s":
#         break
#     else:
#         listB.append(x)
# n = 0
# while n < len(listA):
#     if listA[n] not in listC:
#         listC.extend (listA[n])
#     n += 1
# n = 0
# while n < len(listB):
#     if listB[n] not in listC:
#         listC.extend (listB[n])
#     n += 1
# if listC == []:
#     print('Não há valores informados')
# else:
#     print(f'Os valores unificados das duas listas são: {listC}')

### Remoção de elementos da lista

## del = deletar listas
## range = gera uma sequência de elementos

### Usando listas como filas

## pop = retorna valor do elemento e o exclui da fila

# último = 10
# fila = list(range(1, último + 1))
# while True:
#     print(f'\nExistem {len(fila)} clientes na fila')
#     print(f'Fila atual: {fila}')
#     print('Digite F para adicionar um cliente ao fim da fila,\nou A para realizar o atendimento, S para sair.\n')
#     operação = str(input('Operação (F, A ou S): '))
#     if operação.lower() == 'a':
#         if len(fila) > 0:
#             atendido = fila.pop(0)
#             print(f'Cliente {atendido} atendido')
#         else:
#             print('Fila vazia! Ninguém para atender.')
#     elif operação.lower() == 'f':
#         último += 1
#         fila.append(último)
#     elif operação.lower() == 's':
#         break
#     else:
#         print('Operação inválida! Digite apenas F, A ou S!')

# último = 10
# fila = list(range(1, último + 1))
# while True:
#     print(f'\nExistem {len(fila)} clientes na fila')
#     print(f'Fila atual: {fila}')
#     print('Digite F para adicionar um cliente ao fim da fila\nou A para realizar o atendimento.\n')
#     sair = str(input('Pressione S para sair ou ENTER para continuar: '))
#     if sair.lower() == 's':
#         break    
#     operação = str(input('Operação (F ou A): '))
#     listA = list(operação)
#     while len(listA) > 0:
#         fatia_string = listA[0]
#         del listA[0]
#         if fatia_string.lower() == 'a':
#             if len(fila) > 0:
#                 atendido = fila.pop(0)
#                 print(f'Cliente {atendido} atendido')
#             else:
#                 print('Fila vazia! Ninguém para atender.')
#         elif fatia_string.lower() == 'f':
#             último += 1
#             fila.append(último)
#         else:
#             print('Operação inválida! Digite apenas F ou A!')

# último1 = 10
# último2 = 10
# fila1 = list(range(1, último1 + 1))
# fila2 = list(range(1, último2 + 1))
# while True:
#     print(f'\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} clientes na fila 2')
#     print(f'Fila 1 atual: {fila1}\nFila 2 atual: {fila2}')
#     print('Digite F para adicionar um cliente ao fim da fila 1\nou A para realizar o atendimento.\nDigite G para adicionar um cliente ao fim da fila 2\nou B para realizar o atendimento.\n')
#     sair = str(input('Pressione S para sair ou ENTER para continuar: '))
#     if sair.lower() == 's':
#         break    
#     operação = str(input('Operação (F, A, G, B): '))
#     listA = list(operação)
#     while len(listA) > 0:
#         fatia_string = listA[0]
#         del listA[0]
#         if fatia_string.lower() == 'a':
#             if len(fila1) > 0:
#                 atendido = fila1.pop(0)
#                 print(f'Cliente {atendido} atendido')
#             else:
#                 print('Fila 1 vazia! Ninguém para atender.')
#         elif fatia_string.lower() == 'b':
#             if len(fila2) > 0:
#                 atendido = fila2.pop(0)
#                 print(f'Cliente {atendido} atendido')
#             else:
#                 print('Fila 2 vazia! Ninguém para atender.')
#         elif fatia_string.lower() == 'f':
#             último1 += 1
#             fila1.append(último1)
#         elif fatia_string.lower() == 'g':
#             último2 += 1
#             fila2.append(último1)
#         else:
#             print('Operação inválida! Digite apenas F, A, G, B!')

### Uso de listas como pilhas

# prato = 5
# pilha = list(range(1, prato + 1))
# while True:
#     print(f'\nExistem {len(pilha)} pratos na pilha')
#     print(f'Pilha atual: {pilha}')
#     print('Digite E para empilhar um novo prato,\nou D para desempilhar. S para sair.')
#     operação = input('Operação (E, D ou S): ')
#     if operação.lower() == 'd':
#         if len(pilha) > 0:
#             lavado = pilha.pop(-1)
#             print(f'Prato {lavado} lavado')
#         else:
#             print('Pilha vazia! Nada para lavar.')
#     elif operação.lower() == 'e':
#         prato += 1 #Novo prato
#         pilha.append(prato)
#     elif operação.lower() == 's':
#         break
#     else:
#         print('Operação inválida! Digite apenas E, D ou S.')

# expressao = input("Digite a expressão: ")
# pilha = []
# i = 0
# erro = False

# while i < len(expressao) and not erro:
#     caracter = expressao[i]
#     if caracter == '(':
#         pilha.append(caracter)
#         i += 1
#     elif caracter == ')':
#         if len(pilha) > 0 and pilha[-1] == '(':
#             pilha.pop()
#             i += 1
#         else:
#             erro = True
#     else:
#         i += 1

# if erro or len(pilha) > 0:
#     print("Erro: a ordem dos parênteses está incorreta!")
# else:
#     print("Os parênteses foram abertos e fechados corretamente!")

### Pesquisa

# L = [15, 7, 27, 39]
# p = int(input('digite o valor a procurar: '))
# achou = False
# x = 0
# while x < len(L):
#     if L[x] == p:
#         achou = True
#         break
#     x += 1
# if achou:
#     print(f'{p} achado na posição {x}')
# else:
#     print(f'{p} não encontrado')

# L = [15, 7, 27, 39]
# p = int(input('digite o valor a procurar: '))
# x = 0
# while x < len(L):
#     if L[x] == p:
#         print(f'{p} achado na posição {x}')
#         break
#     x += 1k
# else:
#     print(f'{p} não encontrado')

# L = [15, 7, 27, 39]
# p = int(input('digite o 1º valor a procurar: '))
# v = int(input('digite o 2º valor a procurar: '))
# x = 0
# y = 0
# while x < len(L):
#     if L[x] == p:
#         print(f'{p} achado na posição {x}')
#         break
#     x += 1
# else:
#     print(f'{p} não encontrado')

# while y < len(L):
#     if L[y] == v:
#         print(f'{v} achado na posição {y}')
#         break
#     y += 1
# else:
#     print(f'{v} não encontrado')

# if x < y:
#     print(f'{p} foi encontrado primeiro.')
# elif x > y:
#     print(f'{v} foi encontrado primeiro.')

### Usando for

# L = [8, 9, 15]
# for e in L:
#     print(e)

# L = [7, 9, 10, 12]
# p = int(input('digite um número a pesquisar: '))
# for e in L:
#     if e == p:
#         print('Elemento encontrado!')
#         break
# else:
#     print('Elemento não encontrado.')

# último1 = 10
# último2 = 10
# fila1 = list(range(1, último1 + 1))
# fila2 = list(range(1, último2 + 1))

# for i in range(5): # Repete o menu principal 5 vezes
#     print(f'\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} clientes na fila 2')
#     print(f'Fila 1 atual: {fila1}\nFila 2 atual: {fila2}')
#     print('Digite F para adicionar um cliente ao fim da fila 1\nou A para realizar o atendimento.\nDigite G para adicionar um cliente ao fim da fila 2\nou B para realizar o atendimento.\n')
#     sair = str(input('Pressione S para sair ou ENTER para continuar: '))
#     if sair.lower() == 's':
#         break    
#     operação = str(input('Operação (F, A, G, B): '))
#     for fatia_string in operação:
#         if fatia_string.lower() == 'a':
#             if len(fila1) > 0:
#                 atendido = fila1.pop(0)
#                 print(f'Cliente {atendido} atendido')
#             else:
#                 print('Fila 1 vazia! Ninguém para atender.')
#         elif fatia_string.lower() == 'b':
#             if len(fila2) > 0:
#                 atendido = fila2.pop(0)
#                 print(f'Cliente {atendido} atendido')
#             else:
#                 print('Fila 2 vazia! Ninguém para atender.')
#         elif fatia_string.lower() == 'f':
#             último1 += 1
#             fila1.append(último1)
#         elif fatia_string.lower() == 'g':
#             último2 += 1
#             fila2.append(último1)
#         else:
#             print('Operação inválida! Digite apenas F, A, G, B!')

## se não for possível saber qual o número de repetições desejados, é melhor usar while.

### Range

### Enumerate

lugares_vagos = [10, 2, 1, 3, 0] 
while True: 
    sala= int(input( "Sala (0 sai): ")) 
    if sala== 0: 
        print("Fim") 
        break 
    if sala> len(lugares_vagos) or sala< 1: 
        print("Sala inválida") 
    elif lugares_vagos[sala - 1] == 0: 
        print( "Desculpe, sala lotada! ") 
    else: 
        lugares= int(input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos):")) 
        if lugares> lugares_vagos[sala - 1]: 
            print("Esse número de lugares não está disponível.") 
        elif lugares< 0: 
            print("Número lnválido") 
        else: 
            lugares_vagos[sala - 1] -= lugares 
            print(f"{lugares} lugares vendidos") 
print("Utilização das salas") 
for x, l in enumerate(lugares_vagos): 
    print(f"Sala {x + 1} - {l} lugar(es) vazio(s)")