#while - enquanto

#while condição:
#   print('Olá mundo')

#ex2
#while 10 < 20:
#   print('olá mundo')

#ex2
num = 0
while num < 20:
    print(num)
    num += 1

#ex3
res = 'S'
while res == 'S':
    num = int(input('digite: '))
    if num >= 999:
        print('número muito grande')
        break
    res = str(input('deseja continuar? (S/N): '))

#ex4
while True :
    ini = str(input('digite começar: '))
    if ini != 'começar':
        print('não digitou começar')
    else:
        break