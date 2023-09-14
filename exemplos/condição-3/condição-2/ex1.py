time1 = int(input('Informe os gols do jogo de futebol do primeiro time: '))
time2 = int(input('Informe os gols do jogo de futebol do segundo time: '))

if time1 > time2:
    print('vitória do time 1')
elif time1 < time2:
    print('vitória do time 2')
else:
    print('Empate')