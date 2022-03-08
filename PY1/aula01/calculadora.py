print('---- CALCULADORA INTELIGENTE -----')
valor1 = int(input('Informe um numero inteiro: '))
valor2 = int(input('Informe um outro numero inteiro: '))

operacao = valor1 + valor2 
print('SOMA')
print(str(valor1) + " + " + str(valor2) + " = " + str(operacao))

operacao = valor1 - valor2 
print('SUBTRAÇÃO')
print(str(valor1) + " - " + str(valor2) + " = " + str(operacao))

operacao = valor1 * valor2 
print('MULTIPLICAÇÃO')
print(str(valor1) + " x " + str(valor2) + " = " + str(operacao))

operacao = valor1 / valor2 
print('DIVISÃO')
print(str(valor1) + " / " + str(valor2) + " = " + str(operacao))
