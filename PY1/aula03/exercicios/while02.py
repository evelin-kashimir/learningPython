usuario = ''
senha = ''
saldo = 0

print('PROWAY - TREINAMENTOS, AGORA É BANCO')
print('------------------------------------')
print('              LOGIN')

while(usuario != 'aluno' and senha != 'proway'):
    usuario = input("Usuario: ")
    senha = input("Senha: ")    
    print("Senha ou Usuário incorretos, digite novamente!")

op = 5
while( op != 0):
    print("---------------------------------------")
    print('Olá Aluno, O que deseja fazer? ')
    print('[1] - DEPOSITAR')
    print('[2] - SACAR')
    print('[3] - VER SALDO')
    print('[4] - TRANSFERIR')
    print('[0] - SAIR')
    op = int(input("-> "))

    match op:
        case 1: 
            deposito = float(input("Depósito: R$"))
            saldo = saldo + deposito 
        case 2:
            if(saldo <= 0):
                print("Você não tem saldo para sacar!")
            else:
                saque = float(input("Valor do saque: R$")) 
                saldo = saldo - saque
        case 3:
            print("SALDO: R$" + str(saldo))
        case 4:
            print("TRANFERÊNCIA")
            conta = input("Conta de destino: ")
            transf = float(input("Valor: R$"))
            saldo = saldo - transf
        case 0: 
            print("Saindo...")
        case outroCaso: 
            print("Opção inválida, tente novamente!")