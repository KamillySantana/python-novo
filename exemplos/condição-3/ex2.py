num = float(input('Informe um numero: '))
num2 = float(input('Informe um segundo numero: '))

if num > num2:
    print(f'{num} é maior que {num2}')
elif num < num2:
    print(f'{num2} é maior que {num}')
else:
    print('Os dois são iguais')