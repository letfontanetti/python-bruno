#Faça um programa que tenha uma função chamada ficha(),
#que receba dois parâmetros opcionais: o nome de um jogador
#e quantos gols ele marcou. O programa deverá ser capaz de mostrar
#a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome, gols):
    print(f'o jogador {nome} marcou {gols} gols')

nomejogador = input('digite o nome do jogador: ')
golsmarcados = int(input('digite a quantidade de gols marcados: '))
ficha(nomejogador, golsmarcados)
