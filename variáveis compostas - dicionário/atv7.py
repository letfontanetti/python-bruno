#Crie um programa onde 4 jogadores joguem um dado e tenham resultados
#aleatórios (utilize o metodo randint do import random).
#Guarde esses resultados em um dicionário em Python. No final mostre quanto
#cada um dos jogadores tirou

from random import randint

jogadores = {'jogador 1': randint(1,6), 'jogador 2': randint(1,6), 'jogador 3': randint(1,6), 'jogador 4:': randint(1,6)}
print(jogadores)

