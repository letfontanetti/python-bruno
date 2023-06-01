#Escreva um programa que mostre todos os números entre 5 e 100
# que são divisíveis por 7, mas não são múltiplos de 5.
# Os números obtidos devem ser impressos em sequência.
# E no final mostre a quantidade de números.

qnum = 0
for n in range(1, 101):
    if n % 7 == 0 and n % 5 != 0:
        qnum += 1
        print(n)
print('Quantidade de números: ',qnum)