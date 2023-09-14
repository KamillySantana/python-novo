valor = float(input('Informe o valor de compra: '))
pres = int(input('Informe a quantidade de prestações: '))

conta = valor / pres

if conta >= 500:
    print('O usuário não consegue pagar')
    print(f'Valor da prestação: {conta}')
else:
    print('O usuario consegue pagar')
    print(f'Valor da prestação: {conta}')