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
L = [1, 7, 2, 4]
minimo = L[0]
for e in L:
    if e < minimo:
        minimo = e
print(minimo)

# Exercício 6.13
T = [-10, -8, 0, 1, 2, 5, -2, -4]
minimo = T[0]
maximo = T[0]
for e in T:
    if e < minimo:
        minimo = e
    elif e > maximo:
        maximo = e
print(f"""
Máximo: {maximo} 
Mínimo: {minimo} 
Média: {(minimo + maximo)/2}
""")

# Exercício 6.16
L = [7, 4, 3, 12, 8]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] < L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(e)
    
# Exercício 6.17
estoque = {'tomate': [1000, 2.30],
           'alface': [500, 0.45],
           'batata': [200, 1.20],
           'feijão': [100, 1.50]}
vendas = []
while True:
    entrada = str(input('Digite o nome do produto a adicionar\ne "fim" para continuar: '))
    for e in estoque:
        if entrada.lower() == e:
            entrada_quantidade = int(input('Digite a quantidade: '))
            vendas.append([entrada, entrada_quantidade])
    if entrada not in estoque.keys() and entrada != 'fim':
        print('Produto não existe!')
    if entrada.lower() == 'fim':
        break
total = 0
print('Vendas:\n')
for operação in vendas:
    produto, quantidade = operação
    preço = estoque[produto][1]
    custo = preço * quantidade
    print(f'{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}')
    estoque[produto][0] -= quantidade
    total += custo
print(f' Custo total: {total:21.2f}\n')
print('Estoque:\n')
for chave, dados in estoque.items():
    print('Descrição: ', chave)
    print('Quantidade: ', dados[0])
    print(f'Preço: {dados[1]:6.2f}')