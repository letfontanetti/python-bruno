#.Faça um programa que leia 2 notas de um aluno, calcule a média e
# imprima aprovado ou reprovado(para ser aprovado a média deve ser no mínimo 6

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))

media = n1 + n2 / 2

if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')