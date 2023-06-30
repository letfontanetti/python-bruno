#Faça um programa que tenha uma função chamada área(), que receba as
#dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    area = largura * comprimento

largura = float(input("Digite a largura do terreno em metros: "))
comprimento = float(input("Digite o comprimento do terreno em metros: "))

resultado = area(largura, comprimento)
print("A área do terreno é:", resultado, "metros quadrados.")