#Sistema de pedidos em restaurante: Desenvolva um programa para gerencia
#pedidos em um restaurante. Utilize tuplas para representar cada pedido,
#armazenando informações como número do pedido, itens solicitados e valor total.
#O programa deve permitir registrar 3 pedidos.

pedido1= ( "Pedido 26", "Batata-frita, X-Bacon, Refri 300ml", "R$35,00\n")
pedido2= ( "Pedido 27", "Pizza 8 pedaços: Meia Clabresa e Meia Quatro queijos", "R$45,00\n")
pedido3= ( "Pedido 28", "Salada Caesar", "R$22,00\n")
pedidos= pedido1 + pedido2 + pedido3
print(pedido1, pedido2, pedido3)
for i in pedidos:
    print(i)