#simples

idade = int(input('Digite sua idade: '))
if idade < 20:
    print('Você é novo')
else:
    print('Você é velho')

#simples

nome = str(input('Digite seu nome: '))
if nome == 'Leticia':
    print('Filha de Samuca e Igão')

#lower = deixa maiusculo / ex: if nome lower() == 'leticia'
#upper = deixa minusculo / ex: if nome upper() == 'LETICIA'

#ex num
num = int(input('Digite sua idade: '))
if num %2 == 0:
    print('Par')
else:
    print('Impar')

#ex idade

idade = int(input('Digite sua idade'))
if idade <= 20:
    print('Você é novo')
elif idade >= 70:
    print('Você é velho')
else:
    print('Você é adulto')