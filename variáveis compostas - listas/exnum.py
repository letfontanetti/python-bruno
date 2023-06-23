#lista numerica
num1 = [7, 5, 3, 0, 9, 6]
num1.sort() #imprime numeros aleeatorios
num1.sort(reverse= True) #imprime os numeros em ordem decrescente (aceita string)

#soma
soma = sum(num1) #função de soma
print(f'soma: {soma}')

#maior
maior = max(num1)
menor = min(num1)
print(f'maior : {maior}')
print(f'menor : {menor}')

#atalho para 'num1'
num2 = num1[:] #copia de 'num1' p armazenar em 'num2'
num2[1] = 2
print(f'lista1 : {num1}')
print(f'lista2 : {num2}')

#
num1 = []
while True:
    num1.append(int(input('digite um número: ')))
    res = str(input('deseja continuar[S/N]'))
    if res in 'Nn':
        break
    print(f'os números são {num1}')