print('-' * 20)
print('SENAI legal')
print('-' * 20)

# exemplo é uma rotina pessoal, titulo agora vai ter q ter esse risquinho
# def criar função, sempre la em cima criar a função
# declara função ele pede para dar 2 enter a cada função para separar e não confundi


def linha(): # função sem parametro
    print('-' * 20)

linha() # não precisa mais do print
print('SESI legal')
linha()


print('+=' * 35)


def linha(txt): # com parametro
    print('-' * 20)
    print(txt)
    print('-' * 20)
linha('SESI legal')
linha('SENAI legal')


def soma(a,b): # aqui é fixo 2 valores, obrigatorio passar 2 numeros
    s = a + b
    print('A soma é: ', s)
soma(7, 10)


def soma(*valores): # quantos valores eu quiser, valores idefinidos
    s = 0 # ele vai soma todos os valores que eu informar
    for c in valores:
        s += c
    print('A soma é:', s)
soma(300, 2, 800)
soma(5045, 890, 2, 1, 7)


def soma(a,b=0): # aqui c n passar o segundo valor, o é b=0
    s = a + b
    print('A soma é: ', s)
soma(2, 5)
soma(2)


def soma(a,b): # fora da função, pode amarzenar em uma variavel
    s = a + b
    return s
a = soma(1,300)
print('Soma é:', a)



