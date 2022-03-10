print("CALCULADORA INTELIGENTE")
print("[ + ] - SOMA")
print("[ - ] - SUBTRAÇÃO")
print("[ x ] - MULTIPLICAÇÃO")
print("[ / ] - DIVISÃO")
print("[ 0 ] - SAIR " )
ope = input("Escolha uma opção: ")
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

match ope:
    case '+':
        print("Resultado: " + str(num1 + num2))
    case '-':
        print("Resultado: " + str(num1 - num2))
    case 'x':
        print("Resultado: " + str(num1 * num2))
    case '/':
        print("Resultado: " + str(num1 / num2))
    case '0':
        print("Saindo...") 
    case default:
        print("Opção inválida!")
