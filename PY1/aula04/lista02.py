#lista - objeto iterável
lista = ['dois','cinco','sete']
lista.append("três")  #adiona objeto ao final da lista
lista.insert(0, "um") #adiciona um objeto na posição especificada
print(lista) 
lista.sort() #ordena em ordem alfabética ou crescente
print(lista)
lista.sort(reverse=True) #ordena em ordem decrescente
print(lista)
lista.pop(1) #exclui o item na POSIÇÃO especificada, se não houver parametro exclui o ultimo
print(lista)
lista.remove("um") #remove o VALOR especificado
print(lista)

#verifica se algo existe 
if 'quatro' in lista:
    lista.remove('quatro')
else:
    print('quatro nao existe na lista')

if 'dois' in lista:
    lista.remove('dois')
    print('dois foi removido')
else:
    print('dois não existe na lista')

lista[0] = 'segundo' #alterando o valor da posição especificada
print(lista)

#percorrendo uma lista
for x in range(0, len(lista)): #de 0 até o tamanho total da lista
    print(lista[x]) 

for x in range(0, len(lista)): 
    print(str(x+1) + 'º item -> ' + lista[x]) #numerando utilizando o indice do loop