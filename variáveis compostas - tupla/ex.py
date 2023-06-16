#a tupla é imutavel

fruta = ('maçã','banana','abacaxi','uva')
fruta2 = ('laranja', 'morango', 'melancia')
fruta3 = fruta + fruta2
print(fruta3)
for c in fruta3:
    print(c)