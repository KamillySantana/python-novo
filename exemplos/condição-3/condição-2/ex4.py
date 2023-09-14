num = float(input('Informe o primeiro numero: '))
num2 = float(input('Informe o segundo numero: '))
print('Informe uma das quatro operações matemáticas')
solicite = input('adição/A, subtração/S, multiplicação/M, e divisão/D: ')

if solicite.upper() == 'A' or solicite == 'adição':
    adicao = num + num2
    print(adicao)
elif solicite.upper() == 'S' or solicite == 'subtração':
    subtratacao = num - num2
    print(subtratacao)
elif solicite.upper() == 'M' or solicite == 'multiplicação':
    multiplicacao = num * num2
    print(multiplicacao)
elif solicite.upper() == 'D' or solicite == 'divisão':
    divisao = num / num2
    print(divisao)
else:
    print('Operação invalida')