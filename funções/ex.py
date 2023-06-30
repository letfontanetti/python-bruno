#def Linha():
#    print('-'*20)

#Linha()
#print('me amo')
#Linha()

#----------------------------------------------
#def Linha(txt):
#    print('-'*20)
#    print(txt)
#    print('-'*20)
#Linha('me amo')
#Linha('me amo')

#----------------------------------------------
#def Soma(a,b):
#    S = a + b
#    print('a soma é: ', S)
#Soma(a = 1,b = 300)

#----------------------------------------------
#def Soma(*valores):
#   S = 0
#    for c in valores:
#        S += c
#    print('a soma é: ', S)
#num = [7,5,3,0,9,6] OPÇÃO
#Soma(num) OPÇÃO
#Soma(300,2,600)
#Soma(300,2,600,3,5,20,333,148)

#----------------------------------------------
#def Soma(a,b):
#    S = a + b
#    return S
#print('a soma é: ', Soma(1,300))

#----------------------------------------------
def parouimpar(num):
    if num%2 == 0:
        print('é par')
    else:
        print('é ímpar')

A = int(input('digite um número: '))
parouimpar(A)