# Exercício 6.11
último1 = 10
último2 = 10
fila1 = list(range(1, último1 + 1))
fila2 = list(range(1, último2 + 1))

for i in range(5): # Repete o menu principal 5 vezes
    print(f'\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} clientes na fila 2')
    print(f'Fila 1 atual: {fila1}\nFila 2 atual: {fila2}')
    print('Digite F para adicionar um cliente ao fim da fila 1\nou A para realizar o atendimento.\nDigite G para adicionar um cliente ao fim da fila 2\nou B para realizar o atendimento.\n')
    sair = str(input('Pressione S para sair ou ENTER para continuar: '))
    if sair.lower() == 's':
        break    
    operação = str(input('Operação (F, A, G, B): '))
    for fatia_string in operação:
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

# Exercício 6.12
# Exercício 6.13
# Exercício 6.14
# Exercício 6.15
# Exercício 6.16
# Exercício 6.17
# Exercício 6.18
# Exercício 6.19
# Exercício 6.20
