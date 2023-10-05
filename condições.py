#n = int(input('digite um número: '))

#if n == 1:
#    print('amarelo')
#elif n == 2:
#    print('azul')
#elif n == 3:
#    print('verde')
#else:
#    print('sem cor')

n = int(input('digite um número de 1 a 3: '))
match n:
    case 1:
        print('amarelo')
    case 2:
        print('azul')
    case 3:
        print('verde')
    case _:
        print('sem cor')