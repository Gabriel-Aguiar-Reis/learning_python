# Exercício 7.1
primeira_string = str(input('Primeira string: '))
segunda_string = str(input('Segunda string: ')) 
a = 0
while a > -1:
    a = primeira_string.find(segunda_string, a)
    if a != -1:
        print(f"{segunda_string} encontrado na posição {a} de {primeira_string}")
        break

# Exercício 7.2
string1 = str(input("Digite a primeira string: "))
string2 = str(input("Digite a segunda string: "))
string_comum = ""
for n in string1:
    if n in string2 and n not in string_comum:
        string_comum += n
print(f"Resultado: {string_comum}")

# Exercício 7.3
string_a = str(input('Primeira string: '))
string_b = str(input('Segunda string: '))
string_c = ""
for m in string_a:
    if m not in string_b and m not in string_c:
        string_c += m
for m in string_b:
    if m not in string_a and m not in string_c:
        string_c += m
print(f'Resultado: {string_c}')

# Exercício 7.4
string = input("Digite uma string: ")
for m in set(string):
    contagem = string.count(m)
    print(f"{m}: {contagem}")
    
# Exercício 7.5
# Exercício 7.6
# Exercício 7.7
# Exercício 7.8
# Exercício 7.9
# Exercício 7.10