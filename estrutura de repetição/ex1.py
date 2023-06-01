#quantidade de condições finitas de vezes = 'for'
#condição verdadeira = 'while'

#FOR
#for variavel in range(inicio, fim):
#    print('Olá mundo')

#ex1
for n in range(1,6):
    print('Olá mundo!')
print('fim')
#ele não conta o último número(nesse caso o 6)

#2
for n in range(0, 10, 2):
    print(n)
print('fim')

#ex3
for n in range(10,0,-1):
    print(n)
print('fim')

#ex4
i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))

for n in range(i, f, p):
    print(n)