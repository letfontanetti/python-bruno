# Faça um algoritmo que receba um valor de uma compra
# e receba o numero de prestações, apresente o valor das prestações sem juros.
# Se o valor for maior da prestação for maior que 500 diga que o usuário não consegue pagar.

c = float(input('digite o valor da compra: '))
p = int(input('digite a quantidade de prestações: '))

v = c / p

if v > 500:
    print('Você não consegue pagar')
else:
    print("Você consegue pagar")