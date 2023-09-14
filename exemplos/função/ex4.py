def voto(nascimento):
    nascimento = 2023 - idade
    if nascimento >= 18:
        print('Voto obrigatório')
    elif nascimento >= 16 and nascimento < 18:
        print('Voto opicional')
    elif nascimento <= 15:
        print('Voto negado')


idade = int(input('informe o ano que você nasceu: '))
voto(idade)

