#Crie um programa que tenha uma função chamada voto()
#que vai receber como parâmetro o ano de nascimento de uma pessoa,
#retornando um valor literal indicando se uma pessoa tem voto
#NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições

def voto(nascimento):
    idade = 2023 - nascimento

    if idade < 16:
        return 'voto negado'
    elif 16 <= idade < 18 or idade >= 70:
        return 'voto opcional'
    else:
        return 'voto obrigatório'

ano = int(input('digite o ano de nascimento: '))
result = voto(ano)
print(result)