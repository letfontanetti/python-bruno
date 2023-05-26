salario = float(input('Informe seu salário: '))

aumento = float(input('Informe o percentual de aumento: '))

valor_porcentagem = aumento + salario
salario_atual = (valor_porcentagem / 100) + salario

print('Seu salário passou a ser: ', salario_atual)
