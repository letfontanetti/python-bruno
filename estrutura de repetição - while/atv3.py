#Desenvolva um programa que leia vários números até que o usuário digite
# um numero negativo. O programa também encerra se o usuário digita
# o numero 999,isso deve ser uma condição de parada.

while True:
    num = int(input('digite um número: '))
    if num < 0:
        print('número inválido')
        break
    elif num == 999:
        print('número muito grande')
        break
