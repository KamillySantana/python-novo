print('Calcular o aumento salarial')

salario = int(input('Informe o salario: '))
porcentagem = int(input('Informe a porcentagem: '))

calcular = salario * porcentagem
aumento = (calcular / 100) + salario

print(aumento)