#Faça um programa que solicite dois números ao usuário (com decimais)
# Em seguida solicite que o usuário informe o resultado das quatro operações matemáticas
# (adição, subtração, multiplicação e divisão)

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

op = int(input('Digite o número desejado para realizar a respectiva operação\n(1-adição/2-subtração/3-multiplicação/4-divisão): '))

if op == 1:
    print('o resultado da adição é: ', n1 + n2)
elif op == 2:
    print('o resultado da subtração é: ', n1 - n2)
elif op == 3:
    print('o resultado da multiplicação é: ', n1 * n2)
elif op == 4:
    print('o resultado da divisão é: ', n1 % n2)

