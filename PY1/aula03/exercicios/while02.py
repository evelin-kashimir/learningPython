usuario = ''
senha = ''
saldo = 0

print('PROWAY - TREINAMENTOS, AGORA É BANCO')
print('-'.ljust(40, '-'))
print('LOGIN'.center(40, ' '))

usuario = input("Usuario: ") 
senha = input("Senha: ")     
while(usuario != 'aluno' or senha != 'proway'):     
    print("Senha ou Usuário incorretos, digite novamente!")     
    usuario = input("Usuario: ")     
    senha = input("Senha: ")

op = 5
while( op != 0):
    print("-".ljust(30, "-"))
    print('Olá Aluno, O que deseja fazer? ')
    print('[1] - DEPOSITAR')
    print('[2] - SACAR')
    print('[3] - VER SALDO')
    print('[4] - TRANSFERIR')
    print('[0] - SAIR')
    op = int(input("-> "))

    match op:
        case 1: 
            print("-".ljust(30, "-"))
            print("DEPÓSITO".center(30, ' '))
            deposito = float(input("R$"))
            saldo = saldo + deposito 
        case 2:
            print("-".ljust(30, "-"))
            print("SAQUE".center(30, ' '))
            saque = float(input("R$")) 
            if(saque > saldo):
                print("Saldo insulficiente!")
            else:
                saldo = saldo - saque
        case 3:
            print("-".ljust(30, "-"))
            print("SALDO".center(30, ' '))
            print("R$" + str(saldo))
        case 4:
            print("-".ljust(30, "-"))
            print("TRANFERÊNCIA".center(30, ' '))
            conta = input("Conta de destino: ")
            if(len(conta) == 5): #verificando tamanho
                transf = float(input("R$"))
                saldo = saldo - transf
            else:
                print("Conta inválida, conta deve conter ao menos 5 dígitos")
        case 0: 
            print("-".ljust(30, "-"))
            print("Saindo...")
        case outroCaso:
            print("-".ljust(30, "-")) 
            print("Opção inválida, tente novamente!")