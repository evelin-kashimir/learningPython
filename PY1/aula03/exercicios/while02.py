usuario = ''
senha = ''
saldo = 0

print('PROWAY - TREINAMENTOS, AGORA É BANCO')
print('-'.ljust(40, '-'))
print('LOGIN'.center(40, ' '))

while(usuario != 'aluno' and senha != 'proway'):
    usuario = input("Usuario: ")
    senha = input("Senha: ")    
    print("Senha ou Usuário incorretos, digite novamente!")

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
            if(saldo <= 0):
                print("Você não tem saldo para sacar!")
            else:
                print("-".ljust(30, "-"))
                print("SAQUE".center(30, ' '))
                saque = float(input("R$")) 
                saldo = saldo - saque
        case 3:
            print("-".ljust(30, "-"))
            print("SALDO".center(30, ' '))
            print("R$" + str(saldo))
        case 4:
            print("-".ljust(30, "-"))
            print("TRANFERÊNCIA".center(30, ' '))
            conta = input("Conta de destino: ")
            transf = float(input("R$"))
            saldo = saldo - transf
        case 0: 
            print("-".ljust(30, "-"))
            print("Saindo...")
        case outroCaso:
            print("-".ljust(30, "-")) 
            print("Opção inválida, tente novamente!")