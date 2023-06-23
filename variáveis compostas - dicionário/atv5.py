#Faça um programa que o usuário vai criar um dicionário de notas.
#Ele poderá digitar a quantidade de notas que ele quiser, para parar
#ele deve responder um pergunta S/N. Ao final mostre a media das notas.

dicionario = []

while True:
    notas = int(input("Digite uma nota: "))
    dicionario.append(notas)

    resposta = input("Deseja inserir outra nota? (S/N): ")
    if resposta.upper() != "S":
        break

media = sum(dicionario) / len(dicionario)
print(f"A média das notas é: {media}")