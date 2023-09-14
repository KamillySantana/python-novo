#um loop invinito quando a condição for verdadeira ou as vezes finito
#for variavel in range (inicio, fim): "onde ele começa e aonde ele termina, quando é finito"

for i in range (1,6):
    print('Olá, mundo!')
print('FIM')

for num in range (1,6): #ele vai imprimi o 1 e armazena no num, vai imprimi o 2 e armazena no num no lugar do 1
    print(num) #assim sucessivamente até chega no limite que e 6 e sai do loop
print('FIM')

for n in range (0,10,2): #imprimi de 2 em 2
    print(n)
print('FIM')

for ne in range (10,0,-1): #o primeiro numero é o que ele começa: 10, o segundo é o que ele termina: 0 e o terceirro é o passo que ele vai usa: -1
    print(ne)
print('FIM')

ini = int(input('inicio'))
f = int(input('fim'))
p = int(input('passo'))

for repe in range (ini,f,p):
    print(repe)





