#normal (menor que 37,2 C)
#estado febril (37,3 C a 38 C )
#febre (38 C a 39 C)
#febre alta(acima 39 C)

c = int(input('Infirme a quantidade de clientes: '))
soma = 0
for n in range(1, c+1):
    temp = float(input('Informe a temperatura: '))
    soma += temp
    if temp < 37.2:
        print('Normal')
    elif temp >= 37.3 and temp < 38:
        print('Estado febril')
    elif temp >=38 and temp <= 39:
        print('Febre')
    elif temp > 39:
        print('Febre alta')
media = soma/c
print('A média das temperaturas é', media, 'e a quantidade de clientes é', c)