nome = input('digite seu nome: ')
if nome == 'Yan':
    print('Filho do Bruno')

idade = int(input('digite sua idade: '))
if idade < 20:
    print('Você é novo')
elif idade >= 60:
    print('Você é velho')
else:
    print('Você é adulto')

peso = int(input('digite o seu peso: '))
print(nome, idade, peso)

idade2 = int(input('digite sua idade: '))
if idade2 <= 20 and idade2 >= 5:
    print('Você é novo')
elif idade2 >= 60 or idade2 <= 100:
    print('Você é velho')