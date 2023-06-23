#Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos digitados
#em ordem crescente

num = []

p = int(input('quantas vezes você ira testar o programa?\n'))

for i in range(p):
    x = int(input('digite algum número\n'))
    if x == 0:
        break
    elif x not in num:
        num.append(x)
num.sort()
print(num)
