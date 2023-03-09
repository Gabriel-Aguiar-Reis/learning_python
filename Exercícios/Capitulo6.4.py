# Exercício 6.18
entrada = str(input('Digite a frase que desejar: '))
dicionario = {}
for e in entrada:
    if e in dicionario:
        dicionario[e] += 1
    else:
        dicionario[e] = 1
print(dicionario)

# Exercício 6.19
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])
c = a - b
d = b - a
e = a | b
print(f"""\nValores comuns às duas listas: {e - c - d}
Valores que só existem na primeira lista: {c}
Valores que só existem na segunda lista: {d}
Valores não repetidos: {c | d}
Primeira lista sem elementos repetidos da segunda: {e}""")

# Exercício 6.20
lista1 = set([1, 2, 3, 4, 5])
lista2 = set([1, 9, 3, 7, 5, 6, 10])
m = lista1 - lista2
n = lista2 - lista1
o = lista1 | lista2
print(f"""\nElementos que não mudaram: {o - m - n}
Novos elementos: {n}
Elementos que foram removidos: {m}""")