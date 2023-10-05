#Escreva uma função que aceite um dia da semana (string) e use o match-case
#para verificar se é um dia útil ("segunda", "terça", etc.) ou fim de semana
#("sábado" ou "domingo"). Retorne uma mensagem apropriada para cada dia.

diaS = str(input('informe um dia da semana: '))
match diaS:
    case 'segunda'|'terça'|'quarta'|'quinta'|'sexta':
        print(f'{diaS}, é dia útil')
    case 'sabádo'|'domingo':
        print(f'{diaS}, é final de semana')