#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final mostre:
#-Qual é o total de gasto na compra.
#-Qual o nome do produto mais caro

vcaro = 0
ncaro = ''
total = 0
while True:
    produto = input('qual o produto que deseja comprar: ')
    valor = float(input('qual o valor desse produto: '))
    if valor > vcaro:
        vcaro = valor
        ncaro = produto
        total += valor
        continua = input('deseja continuar? [s/n]: ')
        if continua != 's':
            break
print('o total de sua compra foi: ', total)
print('o produto maius caroi foi: ', ncaro)