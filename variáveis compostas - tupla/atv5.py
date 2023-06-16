#Controle de estoque: Desenvolva um programa para controle de estoque de uma loja.
# Utilize uma tupla para representar cada item do estoque, armazenando informações
# como nome do produto, quantidade disponível e preço unitário.
# O programa deve armazenar 4 itens, ao final mostre o 4 itens e suas informações.

item1 = ('computador', '6', '1.345,00\n')
item2 = ('teclado', '3', '466,00\n')
item3 = ('mouse', '8', '245,00\n')
itens = item1 + item2 + item3
for i in itens:
    print(i)

