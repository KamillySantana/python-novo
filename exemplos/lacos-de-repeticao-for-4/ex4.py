conta = 0

for num in range (5,101,):
    if num % 7 == 0 and num % 5 != 0:
        print(num)
        conta = conta + 1

print(f'A quantidade de números que são divisíveis por 7, mas não são múltiplos de 5 é {conta}')
