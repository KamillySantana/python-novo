soma = 0
produto_mais_caro = 0
nome_do_produto_mais_caro = ''
resp = 'S'

while resp.upper() == 'S':
    nome_produto = input('Nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    soma += preco

    if preco > produto_mais_caro:
        nome_do_produto_mais_caro = nome_produto
        produto_mais_caro = preco

    resp = input('Deseja continuar (S/N): ')

print(f'Total de gasto na compra: {soma}')
print(f'O produto mais caro foi: {nome_do_produto_mais_caro}')
