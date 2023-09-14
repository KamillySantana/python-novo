soma = 0
conta = 0
nota = 0
while nota >= 0:
    nota = float(input('Digite notas (negativo para parar): '))
    if nota >= 0:
        soma += nota
        conta += 1
    else:
        print('Nota negativa')

if conta > 0:
    media = soma / conta
    print("A média das notas é:", media)