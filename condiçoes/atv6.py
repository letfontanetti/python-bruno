#Desenvolva um programa que recebe do usuário, o placar de um jogo de futebol (os gols de cada time)
# e informa se o resultado foi um empate
# se a vitória foi do primeiro time ou do segundo time.

t1 = int(input('Digite a uantidade de gols do primeiro time: '))
t2 = int(input('Digite a quantidade de gols do segundo time: '))

if t1 == t2:
    print("O resultado do jogo foi empate")
elif t1 > t2:
    print("Vitória do primeiro time")
else:
    print("Vitória do segundo time")