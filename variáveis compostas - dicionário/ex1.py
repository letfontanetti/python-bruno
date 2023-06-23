dicio = {}

while True:
    a = str(input('digite a chave: '))
    dicio[a] = str(input('digite o valor: '))
    res = str(input('deseja continuar S/N: '))
    if res in 'Nn':
        break
print(dicio)