nota1 = float(input('Informe a sua primeira nota: '))
nota2 = float(input('Informe a sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 6:
    print(f'{media} Aprovado')
elif media < 6:
    print(f'{media} Reprovado')

