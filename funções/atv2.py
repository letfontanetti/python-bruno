#Faça um programa que tenha uma função chamada escreva(),
#que receba um texto qualquer como parâmetro e mostre uma
#mensagem com tamanho adaptável.

def escreva(txt):
    print('-'*len(txt))

txt = str(input('digite um texto: '))
txt = escreva(txt)

