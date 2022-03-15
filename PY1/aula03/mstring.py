#FORMATANDO STRING

#centralizando string
print("Evelin".center(30, '-'))

#alinhamento a esquerda
print('|1- Sacar'.ljust(30,' ')+ "|") 

nome1 = input("Primeiro nome: ")
nome2 = input("Segundo nome: ")
nome3 = input("Terceiro nome: ")
nome4 = input("Quarto nome: ")

print(nome1.ljust(30, ' ')+ '|')
print(nome2.ljust(30, ' ')+ '|')
print(nome3.ljust(30, ' ')+ '|')
print(nome4.ljust(30, ' ')+ '|')

print('|' +nome1.rjust(30, ' '))
print(nome1.center(30, ' '))