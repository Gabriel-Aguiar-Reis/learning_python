# Exercício 4.2
a=int(input(" write the first number: "))
b=int(input(" write the second number: "))
c=int(input(" write the third number: "))
if a>b and a>c:
    print(f"{a} is the big one")
if b>a and b>c:
    print(f"{b} is the big one") 
if c>a and c>b:
    print(f"{c} is the big one")

# Exercício 4.3
speed=int(input("what's your car speed: "))
if speed>80:
    valor_multa=(speed-80)*5
    print(f"now, you've to pay a traffic ticket of {valor_multa} bucks, idiot")
if speed<=80:
    print("it's all okay")


# Exercício 4.4
wage=int(input("wage = "))
base=wage
wage_increase=0
if base>1250:
    wage_increase=wage_increase+base*0.1
if base<=1250:
    wage_increase=wage_increase+base*0.15
print(f'{wage_increase} is the increase value')

# Exercício 4.6
distance=float(input("what distance do you wanna travel, in km? "))
base=distance
travel_value=0
if base>200:
    travel_value=travel_value+(base-200)*0.45
    base=200
if base<=200:
    travel_value=travel_value+base*0.5
print(f"the travel's value is $ {travel_value:5.2f}")

# Exercício 4.8
a=float(input('primeiro número: '))
operação=str(input('operação desejada (+,*,/,-): '))
b=float(input('segundo número: '))
resultado=0
if operação=='+':
    resultado=a+b
elif operação=='-':
    resultado=a-b
elif operação=='/':
    resultado=a/b
elif operação=='*':
    resultado=a*b
else:
    print('o valor preenchido é inválido')
    resultado=0
print(f'seu resultado é {resultado:.3f}')

# Exercício 4.9
house_value=float(input('house value: '))
wage=float(input('your wage: '))
amount_of_years=int(input('amount of paying years: '))
monthly_installment_value=house_value/(amount_of_years*12)
if monthly_installment_value<=(wage*0.3):
    print('the bank loan was successful')
    print(f'the montlhy amount to be paid is ${monthly_installment_value:.2f}')
else:
    print('the bank loan has been denied')

# Exercício 4.10
khw=float(input('KWh cosumidos: '))
tipo=str(input('tipo de instalação (R, C ou I): '))
preço=0
if tipo=='R' and khw<=500:
    preço=0.4*khw
elif tipo=='R' and khw>500:
    preço=0.65*khw
elif tipo=='C' and khw<=1000:
    preço=0.55*khw
elif tipo=='C' and khw>1000:
    preço=0.6*khw
elif tipo=='I' and khw<=5000:
    preço=0.55*khw
elif tipo=='I' and khw>5000:
    preço=0.6*khw
print(f'valor a pagar R${preço:5.2f}')