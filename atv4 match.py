#Dado o nome de um animal, use o match-case para verificar se é "vaca",
# "galinha" ou "ovelha". Para qualquer outro animal, retorne "Animal desconhecido".

animal = str(input('informe um animal: '))
match animal:
    case 'vaca':
        print('brandão')
    case 'galinha':
        print('frango')
    case 'ovelha':
        print('nuvenzinha')
    case _:
        print('animal desconhecido')