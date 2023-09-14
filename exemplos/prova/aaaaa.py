quant_de_casos = int(input('Informe a quantidade de casos: '))

for caso in range(quant_de_casos):
    print(f"\nCaso {caso+1}:")
    quantidade_de_filtros = int(input('Informe a quantidade de filtros de linha: '))

    total_tomadas = 0  # Variável de contagem inicializada como zero

    for filtro in range(quantidade_de_filtros):
        tomadas = int(input(f'Informe as tomadas de cada filtro {filtro+1}: '))
        total_tomadas += tomadas  # Incrementa o total_tomadas com o número de tomadas informado

    print(f'O total de tomadas no caso {caso+1} é: {total_tomadas}')