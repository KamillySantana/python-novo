# tupla não muda
# ela não vai receber nada, ela não muda diferente de lista
fruta = ('maça', 'banana', 'abacaxi', 'uva')
print(fruta)

# vai printa só a maça
print(fruta[0])

# da pra somar tuplas assim, criando uma nova
fruta2 = ('laranja', 'morango', 'melancia')
fruta3 = fruta + fruta2
print(fruta3)

#printa 1 por 1
for i in range(0,7):
    print(fruta3[i])

print('=' * 15)

# outro for
for c in (fruta3):
    print(c)

print('=' * 15)

#prints
print(fruta3[4]) #laranja
print(fruta3[0:4]) #do maça ao uva
print(fruta[1:]) #todas as frutas
print(fruta3[-1]) #melancia
print(len(fruta3)) # conta a quantidade de frutas

print('=' * 15)

#ordem alfabética e converte para uma lista
print(sorted(fruta3))

print(fruta3.index('banana')) # 1
print(fruta3.count('banana'))