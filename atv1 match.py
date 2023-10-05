#Escreva uma função que aceite um número inteiro e use o match-case para
# verificar se o número é 1, 2, ou 3. Para qualquer outro número, retorne "Outro número".

n = int(input('informe um número: '))
match n:
    case 1:
        print('número digitado: 1')
    case 2:
        print('número digitado: 2')
    case 3:
        print('número digitado: 3')
    case _:
        print('outro número')