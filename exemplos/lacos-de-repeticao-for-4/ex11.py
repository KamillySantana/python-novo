contaPar = 0
contaImpar = 0
informe = int(input('Informe uma quantidaden de numeros: '))

for num in range (1,informe + 1):
    if num % 2 == 0:
        contaPar = contaPar + 1
    else:
        contaImpar = contaImpar + 1

    print(num)

print(f'Tem {contaPar} numeros pares')
print(f'Tem {contaImpar} numeros impares')