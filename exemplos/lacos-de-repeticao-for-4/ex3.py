somaM = 0
somaH = 0
somaG = 0
quantM = 0
quantH = 0

for media in range (1,11):
    print(f'----- Pessoas {media} -----')
    genero = input('Informe seu sexo (feminino/F) ou (masculino/M): ')
    idade = int(input('Informe sua idade: '))

    if genero == 'feminino' or genero.upper() == 'F':
        somaM += idade
        quantM += 1
    elif genero == 'masculino' or genero.upper() == 'M':
        somaH += idade
        quantH += 1

    somaG += idade

mediaM = somaM / quantM
mediaH = somaH / quantH
mediaG = somaG / 10

print(f'Idade média das mulheres: {mediaM}')
print(f'Idade média dos homens: {mediaH}')
print(f'Idade média do grupo: {mediaG}')