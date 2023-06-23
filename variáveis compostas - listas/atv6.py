#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

numeros = []

while True:
    numeros.append(int(input('digite um número ou zero para encerrar: ')))
    if 0 in numeros:
        break

quantidade = len(numeros)
decrescente = sorted(numeros, reverse=True)
if 5 in numeros:
    print('o número 5 está na lista')

print('quantidade de números: ', quantidade)
print('ordem decrescente: ', decrescente)
