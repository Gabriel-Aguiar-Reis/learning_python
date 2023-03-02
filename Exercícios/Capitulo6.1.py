# Exercício 6.1
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

# Exercício 6.2
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

# Exercício 6.3
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

# Exercício 6.5
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