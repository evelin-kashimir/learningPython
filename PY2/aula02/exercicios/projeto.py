from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
from ContaSalario import ContaSalario
import time 
import os

opc = 5
opc02 = 5

while opc != 0:
    print('-'.ljust(40, '-'))
    print('BANCO PW'.center(40, ' ') + '|')
    print('-'.ljust(40, '-'))
    print('Selecione o tipo de Conta: ')
    print('[1] - Conta Corrente')
    print('[2] - Conta Salário')
    print('[3] - Conta Poupança')
    opc = int(input(' -> '))

    contas = []
    dono = ''
    numero = 0
    saque = 0
    deposito = 0
    saldo = 0

    match opc:
        case 1: 
            dono = input('Nome: ')
            numero = int(input('Numero: '))
            conta = ContaCorrente(dono, numero)
            contas.append(conta)

            while opc02 != 0:
                print('CORRENTE'.center(40, ' ') + '|')
                print('-'.ljust(40, '-'))
                print('[1] - Sacar')
                print('[2] - Depositar')
                print('[3] - Transferir')
                print('[4] - Ver Saldo')
                print('[0] - Voltar ao Menu')
                opc02 = int(input(' -> '))

                match opc02:
                    case 1:
                        os.system('cls')
                        print('SACAR'.center(40, ' ') + '|')
                        print('-'.ljust(40, '-'))
                        saque = int(input('Valor do saque: R$'))
                        print(conta.sacar(saque))

                    case 2:
                        os.system('cls')
                        deposito = int(input('Valor do depósito: R$'))
                        conta.depositar(deposito)

                    case 3: 
                        os.system('cls')
                        print('TRANFERÊNCIA'.center(40, ' ') + '|')
                        print('-'.ljust(40, '-'))
                        contaDestino = int(print('Digite o numero da conta para qual desejar transferir: '))
                        valor = int(input('Valor da tranferência: R$'))
                        print(conta.tranferir(contas, contaDestino, valor))

                    case 4:
                        os.system('cls')
                        print(conta.verSaldo())

                    case 0:
                        os.system('cls')
                        print('Saindo...')

                    case outroCaso: 
                        os.system('cls')
                        print('Opção Inválida.')

        case 2: 
            os.system('cls')
            dono = input('Nome: ')
            numero = int(input('Numero: '))
            conta = ContaSalario(dono, numero)
            contas.append(conta)
            
            while opc02 != 0:
                print('SALÁRIO'.center(40, ' ') + '|')
                print('-'.ljust(40, '-'))
                print('[1] - Sacar')
                print('[2] - Ver Saldo')
                print('[0] - Voltar ao Menu')
                opc02 = int(input(' -> '))

                match opc02:
                    case 1:
                        os.system('cls')
                        print('SACAR'.center(40, ' ') + '|')
                        print('-'.ljust(40, '-'))
                        saque = int(input('Valor do saque: R$'))
                        print(conta.sacar(saque))

                    case 2:
                        os.system('cls')
                        print(conta.verSaldo())

                    case 0:
                        os.system('cls')
                        print('Saindo...')

                    case outroCaso: 
                        os.system('cls')
                        print('Opção Inválida.')

        case 3:
            os.system('cls')
            dono = input('Nome: ')
            numero = int(input('Numero: '))
            conta = ContaPoupanca(dono, numero)
            contas.append(conta)

            while opc02 != 0:
                print('POUPANÇA'.center(40, ' ') + '|')
                print('-'.ljust(40, '-'))
                print('[1]'.ljust(40, ' ')+ 'Sacar|')
                print('[2]'.ljust(40, ' ')+ 'Depositar|')
                print('[3]'.ljust(40, ' ')+ 'Ver Saldo|')
                print('[0]'.ljust(40, ' ')+ 'Voltar ao Menu|')
                opc02 = int(input(' -> '))

                match opc02:
                    case 1:
                        os.system('cls')
                        print('SACAR'.center(40, ' ') + '|')
                        print('-'.ljust(40, '-'))
                        saque = int(input('Valor do saque: R$'))
                        print(conta.sacar(saque))

                    case 2:
                        os.system('cls')
                        print(conta.depositar())

                    case 3:
                        os.system('cls')
                        print(conta.verSaldo())

                    case 0:
                        os.system('cls')
                        print('Saindo...')

                    case outroCaso: 
                        os.system('cls')
                        print('Opção Inválida.')
                        
        case 0:
            os.system('cls')
            print('Saindo...')
        case outroCaso: 
            os.system('cls')
            print('Opção Inválida.')
