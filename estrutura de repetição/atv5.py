#Desenvolva um programa que leia o nome, idade e sexo de 8 pessoas.
# No final do programa mostre:
# -Qual o nome do homem mais velho
# -Quantas mulheres tem menos de 20 anos

idadevelho = 0
nomevelho = ''
mulheres20 = 0
for n in range(0, 9):
    nome = str(input('Informe seu nome: '))
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe seu sexo: '))
    if sexo == 'M' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    elif sexo == 'F' and idade <= 20:
        mulheres20 += 1
print('O mais velho se chama: ',nomevelho)
print('Mulheres que tem menos de 20 anos: ',mulheres20)