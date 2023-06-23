#pessoa = {'nome':'duda', 'idade':16, 'altura':1.50} #nomeando posições
#print(pessoa['nome'])
#pessoa = {}
#pessoa = dict()

#acrescentar elemento
pessoa = {'nome':'duda', 'idade':16, 'altura':1.50}
pessoa2 = {'nome':'brenda', 'peso':60, 'sexo':'F'}
pessoa.update(pessoa2)
pessoa2['peso'] = 52
print(pessoa)

pessoa = {'nome':'duda',
          'idade':16,
          'altura':1.50}
print(pessoa.values()) #imprime só valores
print(pessoa.keys()) #imprime as chaves

for K in pessoa.keys(): #imprime uma chave embaixo da outra
    print(K)

for V in pessoa.values(): #imprime um valor embaixo do outro
    print(V)

for K, V in pessoa.items():
    print(f'o item{K} é {V}')

pessoa = {'nome':'duda', 'idade':16, 'altura':1.50}
idaded = int(input('digite sua idade: '))
if idaded in pessoa.values():
    print('vc tem a mesma idade que a duda')


