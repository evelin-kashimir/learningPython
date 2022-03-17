lista = [5, 3, 5.5, 'oi', True]
lista2 = ['Proway', lista]

print(lista)
print(lista[0])
print(lista2[1])

print(type(lista2[0]))

#verificando se é algo
if type(lista2[0]) is str:
    print(lista2[0] + ' é uma string ')