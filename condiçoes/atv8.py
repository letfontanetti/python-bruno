#Elabore um algoritmo que dada a idade de um nadador
# classifique-o em uma das seguintes categorias:
#Infantil A = 5 a 7 anos
#Infantil B = 8 a 11 anos
#Juvenil A = 12 a 13 anos
#Juvenil B = 14 a 17 anos
#Adultos = Maiores de 18 anos

idade = int(input('Digite sua idade: '))

if idade >= 5 and idade <= 7:
    print("Infantil A")
elif idade >= 8 and idade <= 11:
    print ("Infantil B")
elif idade >= 12 and idade <= 13:
    print ("Juvenil A")
elif idade >= 14 and idade <= 17:
    print ("Juvenil B")
elif idade >= 18:
    print ("Adulto")