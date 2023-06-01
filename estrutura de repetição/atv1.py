#Construa um programa em Python utilizando os comandos aprendidos até agora
# para encontrar todos os números pares entre 1 e 100.
# E no final mostre a quantidade de números

pares = 0
for par in range(1, 101):
    if par % 2 == 0:
        pares += 1
print('existem',pares, 'numeros pares entre 1 e 100')