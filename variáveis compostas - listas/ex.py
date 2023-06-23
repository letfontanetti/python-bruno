fruta = ['maça', 'banana', 'abacaxi', 'uva']

#troca elementos
fruta[3] = 'melancia' #trocar elemento

#add elemento
fruta.append('laranja') #add elemento
fruta.insert(0, 'morango') #add um elemento em determinada opção

#remove elemento
del fruta[3] #remove pela posição
fruta.pop(3) #remove pela posição
fruta.remove('abacaxi') #remove pelo nome
print(fruta)

#remove elemento
if 'abacaxi' in fruta: #remove fruta
    fruta.remove('abacaxi')
else:
    print('não encontrado')

#maior/menor frutas
frutas = ['banana', 'maça', 'laranja', 'abacaxi']
maior = max(frutas, key=len)
menor = min(frutas, key=len)
print(f'maior : {maior}')
print(f'menor : {menor}')