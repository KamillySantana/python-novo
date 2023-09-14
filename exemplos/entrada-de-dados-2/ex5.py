valor = int(input('Informe o valor: '))
taxa = int(input('Informe a taxa: '))
tempo = int(input('Informe o tempo: '))

prestacao = valor + (valor * (taxa/100) * tempo)

print(prestacao)