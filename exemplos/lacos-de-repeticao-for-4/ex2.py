quanClientes = int(input('Informe a quantidade de clientes: '))
soma = 0

for clientes in range (1,quanClientes + 1):
    print(f'----- Pessoas {clientes} -----')
    informe = float(input('Informe a sua temperatura: '))
    soma += informe

    if informe <= 37.2:
        print('Temperatura esta normal')
    elif informe >= 37.3 and informe < 38:
        print('Está em estado febril')
    elif informe >= 38 and informe < 39:
        print('Com febre')
    else:
        print('Febre alta')

media = soma / quanClientes
print(f'Foram {clientes} clientes')
print(f'A média das temperaturas é: {media}')

