# kamilly Santana Alves Ferreira
# bem-vindos e bem-vindas ao inverno!

while True: #primeiramente coloquei um while para fazer um loop das temperaturas maximas e minimas que podem ser ultilizadas
    temperatura = float(input('Informe a temperatura do primeiro dia: '))
    temperatura2 = float(input('Informe a temperatura do segundo dia: '))
    temperatura3 = float(input('Informe a temperatura do terceiro dia: '))

    if temperatura < -100 or temperatura > 100: #se as temperaturas forem menor que menos -100, valor negativo e maior que 100, valor positivo
        print('temperatura invalida, ela deve etar entre -100 e 100') # vai aparecer como temperatura invalida
    elif temperatura2 < -100 or temperatura2 > 100:
        print('temperatura invalida, ela deve etar entre -100 e 100')
    elif temperatura3 < -100 or temperatura3 > 100:
        print('temperatura invalida, ela deve etar entre -100 e 100')
    else: #quando ele informar as temperaturas certas sai do loop
        break
if temperatura > temperatura2 and temperatura2 <= temperatura3: #chegando aqui é para verificar quando as pessoas ficam felizes e tristes com as temperaturas
    print(':)')
elif temperatura < temperatura2 and temperatura2 >= temperatura3:
    print(':(')
elif (temperatura3 - temperatura2) < (temperatura2 - temperatura): #pensei nessa possibilidade de que quando fala que do 2° para o 3° subiu menos do que do 1° para o 2° então é so fazer 2° e 3° menos 2° e 1°
    print(':(')
elif temperatura < temperatura2 and temperatura2 < temperatura3 and (temperatura2 - temperatura) <= (temperatura3 - temperatura2): #fui fazendo por essa mesma lógicas nas seguintes
    print(':)')
elif temperatura > temperatura2 and temperatura2 > temperatura3 and (temperatura - temperatura2) > (temperatura2 - temperatura3):
    print(':)')
elif temperatura > temperatura2 and temperatura2 > temperatura3 and (temperatura - temperatura2) <= (temperatura2 - temperatura3):
    print(':(')
elif temperatura == temperatura2 and temperatura2:
    print(':)')
elif temperatura == temperatura2 and temperatura2 > temperatura3:
    print(':(')