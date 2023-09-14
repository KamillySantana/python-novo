idade = int(input('Informe seu ano de nascimento: '))

calculo = 2023 - idade
print(calculo)
if calculo > 18:
    print('Você é maior de idade')
else:
    print('Você ainda é menor de idade')