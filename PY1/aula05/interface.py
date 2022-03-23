from funcoes import defineOpc

objeto = [1]
n1 = int(input('Informe um valor inteiro: '))
n2 = int(input('Informe outro valor inteiro: '))

objeto.append(n1)
objeto.append(n2)

print('OPÇÕES: ')
print('1 - Soma')
print('2 - Divisão')
opc = int(input('-> '))

defineOpc(objeto,opc)

