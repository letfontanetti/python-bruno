login = str(input('digite seu login: '))
senha = str(input('digite sua senha: '))
match(login,senha):
    case('leticia','2006'):
        print('logado com sucesso')
    case _:
        print('login ou senha incorreto')