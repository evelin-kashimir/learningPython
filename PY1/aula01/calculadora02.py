print("---- CALCULADORA -----")
print("   [+] [-] [x] [/]")

operacao = input("Qual operação deseja realizar: ")
num1 = (int(input("Digite um número: ")))
num2 = (int(input("Digite outro número: ")))

if(operacao == '+'):
    print(num1 + num2)
if(operacao == '-'):
    print(num1 - num2)
if(operacao == 'x'):
    print(num1 * num2)
if(operacao == '/'):
    print(num1 / num2)
##else: print("Operação Inválida!")
