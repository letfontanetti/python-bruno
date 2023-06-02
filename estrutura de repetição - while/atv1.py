#Escreva um programa que solicite ao usuário uma série de notas (números reais)
# e calcule a média dessas notas. O programa deve parar de solicitar notas
# quando o usuário digitar um valor negativo.

soma = 0
qntnotas = 0

while True :
    nota = int(input('digite sua nota: '))
    soma += nota
    qntnotas += 1
    if nota < 0:
        media = soma / qntnotas
        print('sua média é: ', media)
        break