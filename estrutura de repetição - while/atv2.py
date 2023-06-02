#Escreva um programa que solicite ao usuário que digite uma série de números
# e, em seguida, exiba a soma apenas dos números pares digitados.
# O programa deve parar quando o número 0 for digitado.

soma = 0
qntpares = 0
while True:
    num = int(input('digite um número: '))
    if num == 0:
        print('a soma dos números pares é: ', soma)
        break
    elif num %2 == 0:
        soma += num