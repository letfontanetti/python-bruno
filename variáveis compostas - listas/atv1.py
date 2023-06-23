#Escreva um programa que solicite vários números ao usuário, sendo um de cada vez
# possibilitando encerrar a entrada de dados informando zero. Adicione os números
# informados em uma lista e, ao final do programa, imprima a soma de todos os números
# a multiplicação de todos os números, o maior e o menor número informado.

numeros = []
numero = []
multiplicacao = 1

while numero != 0:
    numero = int(input('digite um número ou zero para encerrar: '))
    numeros.append((numero))

numeros.remove(0) #para remover o zero da lista

soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)

for num in numeros:
    multiplicacao*=num

print('soma dos números: ', soma)
print('multiplicação dos números: ', multiplicacao)
print('maior número: ', maior)
print('menor número: ', menor)
