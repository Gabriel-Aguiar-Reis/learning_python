# Exercício 6.6
último1 = 10
último2 = 10
fila1 = list(range(1, último1 + 1))
fila2 = list(range(1, último2 + 1))
while True:
    print(f'\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} clientes na fila 2')
    print(f'Fila 1 atual: {fila1}\nFila 2 atual: {fila2}')
    print('Digite F para adicionar um cliente ao fim da fila 1\nou A para realizar o atendimento.\nDigite G para adicionar um cliente ao fim da fila 2\nou B para realizar o atendimento.\n')
    sair = str(input('Pressione S para sair ou ENTER para continuar: '))
    if sair.lower() == 's':
        break    
    operação = str(input('Operação (F, A, G, B): '))
    listA = list(operação)
    while len(listA) > 0:
        fatia_string = listA[0]
        del listA[0]
        if fatia_string.lower() == 'a':
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f'Cliente {atendido} atendido')
            else:
                print('Fila 1 vazia! Ninguém para atender.')
        elif fatia_string.lower() == 'b':
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f'Cliente {atendido} atendido')
            else:
                print('Fila 2 vazia! Ninguém para atender.')
        elif fatia_string.lower() == 'f':
            último1 += 1
            fila1.append(último1)
        elif fatia_string.lower() == 'g':
            último2 += 1
            fila2.append(último1)
        else:
            print('Operação inválida! Digite apenas F, A, G, B!')

# Exercício 6.7
expressao = input("Digite a expressão: ")
pilha = []
n = 0
erro = False
while n < len(expressao) and not erro:
    caracter = expressao[n]
    if caracter == '(':
        pilha.append(caracter)
        n += 1
    elif caracter == ')':
        if len(pilha) > 0 and pilha[-1] == '(':
            pilha.pop()
            n += 1
        else:
            erro = True
    else:
        n += 1

# Exercício 6.8
L = [15, 7, 27, 39]
p = int(input('digite o valor a procurar: '))
x = 0
while x < len(L):
    if L[x] == p:
        print(f'{p} achado na posição {x}')
        break
    x += 1
else:
    print(f'{p} não encontrado')

# Exercício 6.9
L = [15, 7, 27, 39]
p = int(input('digite o 1º valor a procurar: '))
v = int(input('digite o 2º valor a procurar: '))
x = 0
y = 0
while x < len(L):
    if L[x] == p:
        print(f'{p} achado na posição {x}')
        break
    x += 1
else:
    print(f'{p} não encontrado')

# Exercício 6.10
while y < len(L):
    if L[y] == v:
        print(f'{v} achado na posição {y}')
        break
    y += 1
else:
    print(f'{v} não encontrado')

if x < y:
    print(f'{p} foi encontrado primeiro.')
elif x > y:
    print(f'{v} foi encontrado primeiro.')

