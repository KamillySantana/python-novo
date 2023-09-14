def ficha(nome, gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s)')


nome = input('Informe o nome do jogador: ')
gol = int(input('Informe a quantidade de gols: '))
ficha(nome, gol)
