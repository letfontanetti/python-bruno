#Dado um nome de cor (string), use o match-case para verificar se é "vermelho",
# "azul" ou "verde". Para qualquer outra cor, retorne "Cor desconhecida".

cor = str(input('informe o nome de uma cor: '))
match cor:
    case 'vermelho':
        print('vermelho')
    case 'azul':
        print('azul')
    case 'verde':
        print('verde')
    case _:
        print('cor desconhecida')