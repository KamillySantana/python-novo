while True:
    num = float(input('Informe um numero: '))
    num2 = float(input('Informe um segundo numero: '))
    escolha = int(input('1 - Somar \n2 - Multiplicar \n3 - Subtrair \n4 - Divisão \n5 - Sair do Programa \nEscolha entre: '))

    if escolha == 1:
        conta1 = num + num2
        print(conta1)
    elif escolha == 2:
        conta2 = num * num2
        print(conta2)
    elif escolha == 3:
        conta3 = num - num2
        print(conta3)
    elif escolha == 4:
        conta4 = num / num2
        print(conta4)
    elif escolha == 5:
        break