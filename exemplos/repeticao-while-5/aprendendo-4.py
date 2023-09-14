#while condicao:
#enquanto a condição for verdeira ele executa

# while 10 < 20: #Enquanto 10 for menor que 20, vai printa ola mundo
    # print('Olá, mundo!')

num = 0
while num < 20:
    print(num)
    num += 1

res = 'S'
while res == 'S': #ele vai pedir ao usuario digitar numeros infinitamente, até que o usuario escreva N, para parar o loop
    nume = int(input('Digete: '))
    res = input('Deseja continuar (S/N): ')

resp = 'S'
while resp == 'S':
    numer = int(input('Digete: '))
    if numer == 999:
        print('Numero muito grande')
        break #condição de parada, se cair em 999 vai parar, da para usar no for
    resp = input('Deseja continuar (S/N): ')

#while true
#uma condição verdadeiro ou falso, se colocar true ja esta especifiando que eh verdadeiro

while True:
    ini = input('Digite Começar: ')
    if ini != 'Começar':
        print('Não digitou Começar') # forçar o usuario a digitar começar
    else:
        break
