#Organizador de eventos: Crie um programa para organizar eventos.
# Utilize tupla para representar cada evento, com informações como
# nome, data, local e participantes. Crie 3 eventos e imprima cada um.

evento1 = 'festa poolpaty', '23/06', 'iateclub', 'selecionados\n'
evento2 = 'festa do pijama', '13/09', 'casa', 'migos\n'
evento3 = 'festa de 15 anos', '05/11', 'salão de festas', 'familia\n'
eventos = evento1 + evento2 + evento3
print(eventos)
for f in eventos:
    print(f)