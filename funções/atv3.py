#Faça um programa que tenha uma função chamada maior(),
#que receba vários parâmetros com valores inteiros. Seu programa
#tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    maiorNum = max(num)
    return maiorNum

numeros = maior(6,7,9,5,3)

print(f"O maior número desta sequência é: {numeros}")