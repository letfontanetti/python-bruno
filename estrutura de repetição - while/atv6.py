#Crie um programa que leia dois valores e mostre um menu na tela:
#1 - Somar
#2 - Multiplicar
#3 - Subtrair
#4 - Divisão
#5 - Sair do Programa

num = 0
num2 = 0

while True:
    num = int(input('digite o primeiro numero: '))
    num2 = int(input('digite o segundo numero: '))
    calcular = int(input('qual operação deseja escolher?\nadição(1)\nsubtração(2)\nsubtração(3)\ndivisão(4)\nsair do programa(5)\n'))
    if calcular == 1:
        adicao = num + num2
        print(f'sua operação escolhida foi adição. esse é o resultado {adicao}')
    elif calcular == 2:
        sub = num - num2
        print(f'sua operação escolhida foi subtração. esse é o resultado {sub}')
    elif calcular == 3:
        multi = num * num2
        print(f'sua operação escolhida foi multiplicação. esse é o resultado {multi}')
    elif calcular == 4:
        print(f'sua operação escolhida foi divisão. esse é o resultado {num/num2}')
    elif calcular == 5:
        break