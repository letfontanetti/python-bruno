v = float(input('Informe o valor: '))
tx = int(input('Informe a taxa: '))
t = int(input('Informe o tempo: '))

prestacao = v + (v * (tx / 100) * t)

print('O valor da prestação é:', prestacao)