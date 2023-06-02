#Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M'ou 'F'. Caso esteja errado peça a
# digitação novamente até ter um valor correto.

p = str(input('digite qual o seu sexo: '))
fem = 'f'
mas = 'm'

while p != 'f' and p != 'm':
    p = str(input('digite novamente: '))