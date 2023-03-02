#Exercício 5.1

#Exercício 5.2

#Exercício 5.3
# x=10
# while x>=0:
#     print(x)
#     x=x-1
# else:
#     print('FOGO!')

#Exercício 5.4
# fim = int(input('último número a imprimir: '))
# x=0
# while x <= fim:
#     if x % 2 != 0:
#         print(x)
#     x = x + 1

#Exercício 5.5
# x=0
# while x <= 30:
#     if x % 3 == 0 and x != 0:
#         print(x)
#     x = x + 1

#Exercício 5.6
# n = int(input('Tabuada do número: '))
# x = 1
# while x <= 10:
#     print(f'{n}x{x} = {n * x}')
#     x = x + 1

#Exercício 5.7
# n = int(input('Tabuada do número: '))
# x = int(input('Início da tabuada: '))
# y = int(input('Fim da tabuada: '))
# while x <= y:
#     print(f'{n}x{x} = {n * x}')
#     x += 1

#Exercício 5.8
# a = int(input('primeiro número: '))
# b = int(input('segundo número: '))
# x = a
# y = b
# resultado = 0
# while y > 0:
#     resultado = resultado + x
#     y = y - 1
# print(f'{a}*{b}')
# print(f'O resultado é {resultado}')

#Exercício 5.9
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
# # print(f'O resultado é {resultado_inteiro},\n e o resto é {resto}.')

#Exercício 5.10
# pontos = 0
# questão = 1
# while questão <= 3:
#     resposta = input(f'resposta da questão {questão}: ')
#     if questão == 1 and resposta.lower() == 'b':
#         pontos = pontos + 1
#     if questão == 2 and resposta.lower() == 'a':
#         pontos = pontos + 1
#     if questão == 3 and resposta.lower() == 'd':
#         pontos = pontos + 1
#     questão = questão + 1
# print(f'O aluno fez {pontos} ponto(s)')