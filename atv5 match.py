#Dado um login e senha, use o match-case para verificar se eles correspondem
# a uma das seguintes combinações:
#("admin", "admin_pass")
#("user", "user_pass")
#("guest", _)
#Retorne uma mensagem apropriada para cada combinação, e uma mensagem de erro
# se não houver correspondência.

login = str(input('informe se login: '))
senha = str(input('informe sua senha: '))
match (login,senha):
    case ("admin", "admin_pass"):
        print('bem-vindo admin')
    case ("user", "user_pass"):
        print('bem-vindo user')
    case ("guest", _):
        print('bem-vindo guest')
    case _:
        print('erro ao logar')