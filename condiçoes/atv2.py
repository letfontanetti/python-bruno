# Faça um programa que peça dois números ao usuário
# e mostre qual o maior e qual o menor

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 < n2:
    print('O número', n1, 'é menor que o', n2)
else:
    print('O número', n2, 'é menor que o', n1)