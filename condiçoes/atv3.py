#Escreva um programa em Python que recebe um inteiro e diga se é par ou ímpar

n = int(input('Digite um número: '))

if n %2 == 0:
    print('O número', n, 'é par')
else:
    print('O número', n, 'é impar')
