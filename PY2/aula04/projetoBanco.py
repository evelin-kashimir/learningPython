from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca
from aula04.contaSalario import ContaSalario
import funcoes as f
import constantes as cons

contasC = {} #Conta Corrente
contasS = {} #Conta Salário
contasP = {} #Conta Poupança

op = 0
tipoConta = 0
valor = 0

f.LimpaTela()
while op != 5:
    print('Banco Proway\n'
          '1- Criar Conta\n'
          '2- Listar Contas\n'
          '3- Excluir Conta\n'
          '4- Operações\n'
          '5- Sair\n')
    op = int(input('Informe a opção desejada: '))
    f.LimpaTela()
    match op:
        case 1:            
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            numero = input(cons.MSG_CONTA_PARA_CADASTRAR)
            if (not ( f.EhContaValida(numero) )):
                f.AguardaeLimpa()
            else:
                match tipoConta:
                    case 1:                    
                        if ( not ( f.ExisteConta(numero,contasC,True))):
                            c = ContaCorrente(numero)
                            contasC[c.conta] = 0
                            print(cons.MSG_SUCESSO_CADASTRAR)
                            del(c)
                    case 2:
                        if ( not ( f.ExisteConta(numero,contasS,True) )):
                            c = ContaSalario(numero)
                            contasS[c.conta] = 0
                            print(cons.MSG_SUCESSO_CADASTRAR)
                            del(c)
                    case outrocaso:
                        if ( not ( f.ExisteConta(numero,contasP,True) )):
                            c = ContaPoupanca(numero)
                            contasP[c.conta] = 0
                            print(cons.MSG_SUCESSO_CADASTRAR)
                            del(c)
            f.AguardaeLimpa()
        case 2:
            tipoConta = f.validaTipoConta(True)
            f.LimpaTela()
            match tipoConta:
                case 1:
                    if ( f.ExisteContaCadastrada(contasC,tipoConta) ):
                        print(contasC)
                case 2:
                    if ( f.ExisteContaCadastrada(contasS,tipoConta) ):
                        print(contasS)
                case 3:
                    if ( f.ExisteContaCadastrada(contasP,tipoConta) ):
                        print(contasP)
                case outrocaso:
                    print('Contas Corrente')
                    print(contasC)
                    print('Contas Salário')
                    print(contasS)
                    print('Contas Poupança')
                    print(contasP)
            f.AguardaeLimpa() 
        case 3:
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            match tipoConta:
                case 1:
                    if f.ExisteContaCadastrada(contasC,tipoConta):
                        numero = input(cons.MSG_CONTA_EXCLUIR)
                        if f.EhContaValida(numero):
                            if f.ExisteConta(numero,contasC):
                                c = ContaCorrente(numero)
                                contasC.pop(c.conta)
                                print(cons.MSG_SUCESSO_EXCLUIR)
                                del(c)
                case 2:
                    if f.ExisteContaCadastrada(contasS,tipoConta):
                        numero = input(cons.MSG_CONTA_EXCLUIR)
                        if f.EhContaValida(numero):
                            if f.ExisteConta(numero,contasS):
                                c = ContaSalario(numero)
                                contasS.pop(c.conta)
                                print(cons.MSG_SUCESSO_EXCLUIR)
                                del(c)
                case outrocaso:
                    if f.ExisteContaCadastrada(contasP,tipoConta):
                        numero = input(cons.MSG_CONTA_EXCLUIR)
                        if f.EhContaValida(numero):
                            if f.ExisteConta(numero,contasP):
                                c = ContaPoupanca(numero)
                                contasP.pop(c.conta)
                                print(cons.MSG_SUCESSO_EXCLUIR)
                                del(c)
            f.AguardaeLimpa()
        case 4:
            tipoConta = f.validaTipoConta()
            f.LimpaTela()
            match tipoConta:
                case 1: #Conta Corrente
                    op = f.menuOperacoes(tipoConta)
                    match op:
                        case 1: #Sacar
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.EhContaValida(numero):
                                if f.ExisteConta(numero,contasC):
                                    valor = int(input(cons.MSG_VALOR_SAQUE))
                                    if f.ExisteSaldo(numero,contasC,tipoConta,valor):
                                        contasC[numero] -= (valor + ( valor * 0.05 ))
                                        f.LimpaTela()
                                        print(cons.MSG_SUCESSO_SAQUE)
                                        f.AguardaeLimpa()
                        case 2:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.EhContaValida(numero):
                                if f.ExisteConta(numero,contasC):
                                    valor = int(input(cons.MSG_VALOR_DEPOSITO))
                                    contasC[numero] += valor
                                    f.LimpaTela()
                                    print(cons.MSG_SUCESSO_DEPOSITO)
                                    f.AguardaeLimpa()
                        case 3:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.EhContaValida(numero):
                                if f.ExisteConta(numero,contasC):
                                    numeroDest = input(cons.MSG_NUMERO_CONTA_DESTINO)
                                    tipoDestino = f.validaTipoConta()
                                    match tipoDestino:
                                        case 1:
                                            if f.ExisteConta(numeroDest,contasC):
                                                valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                                                if f.ExisteSaldo(numero,contasC,tipoConta,valor):
                                                    contasC[numero] -= valor
                                                    contasC[numeroDest] += valor
                                        case 2:
                                            if f.ExisteConta(numeroDest,contasS):
                                                valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                                                if f.ExisteSaldo(numero,contasC,tipoConta,valor):
                                                    contasC[numero] -= valor
                                                    contasS[numeroDest] += valor
                                        case outrocaso:
                                            if f.ExisteConta(numeroDest,contasP):
                                                valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                                                if f.ExisteSaldo(numero,contasC,tipoConta,valor):
                                                    contasC[numero] -= valor
                                                    contasP[numeroDest] += valor
                                f.LimpaTela()
                                print(cons.MSG_SUCESSO_TRANSFERENCIA)
                                f.AguardaeLimpa()
                        case 4:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.EhContaValida(numero):
                                if f.ExisteConta(numero,contasC):
                                    f.LimpaTela()
                                    print(contasC[numero])
                                    f.AguardaeLimpa()
                        case outrocaso:
                            break    
                case 2: #Conta Salário
                    op = f.menuOperacoes(tipoConta)
                    match op:
                        case 1:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.EhContaValida(numero):
                                if f.ExisteConta(numero,contasS):
                                    valor = int(input(cons.MSG_VALOR_SAQUE))
                                    if f.ExisteSaldo(numero,contasS,tipoConta,valor):
                                        contasS[numero] -= valor
                        case 2:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.EhContaValida(numero):
                                if f.ExisteConta(numero,contasS):
                                    print(contasS[numero])
                        case outrocaso:
                            break
                case outrocaso: #Conta Poupança
                    op = f.menuOperacoes(tipoConta)
                    match op:
                        case 1: #Sacar
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.EhContaValida(numero):
                                if f.ExisteConta(numero,contasP):
                                    valor = int(input(cons.MSG_VALOR_SAQUE))
                                    if f.ExisteSaldo(numero,contasP,tipoConta,valor):
                                        contasP[numero] -= valor
                                        print(cons.MSG_SUCESSO_SAQUE)
                        case 2:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.EhContaValida(numero):
                                if f.ExisteConta(numero,contasP):
                                    valor = int(input(cons.MSG_VALOR_DEPOSITO))
                                    contasP[numero] += valor
                                    print(cons.MSG_SUCESSO_DEPOSITO)
                        case 3:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.EhContaValida(numero):
                                if f.ExisteConta(numero,contasP):
                                    numeroDest = input(cons.MSG_NUMERO_CONTA_DESTINO)
                                    tipoDestino = f.validaTipoConta()
                                    match tipoDestino:
                                        case 1:
                                            if f.ExisteConta(numeroDest,contasC):
                                                valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                                                if f.ExisteSaldo(numero,contasP,tipoConta,valor):
                                                    contasP[numero] -= valor
                                                    contasC[numeroDest] += valor
                                        case 2:
                                            if f.ExisteConta(numeroDest,contasS):
                                                valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                                                if f.ExisteSaldo(numero,contasP,tipoConta,valor):
                                                    contasP[numero] -= valor
                                                    contasS[numeroDest] += valor
                                        case outrocaso:
                                            if f.ExisteConta(numeroDest,contasP):
                                                valor = int(input(cons.MSG_VALOR_TRANSFERENCIA))
                                                if f.ExisteSaldo(numero,contasP,tipoConta,valor):
                                                    contasP[numero] -= valor
                                                    contasP[numeroDest] += valor
                                f.LimpaTela()
                                print(cons.MSG_SUCESSO_TRANSFERENCIA)
                        case 4:
                            numero = input(cons.MSG_NUMERO_CONTA)
                            if f.EhContaValida(numero):
                                if f.ExisteConta(numero,contasP):
                                    print(contasP[numero])
                        case outrocaso:
                            break    
        case 5:
            print(cons.MSG_ENCERRA_SISTEMA)
            f.AguardaeLimpa()
            break
        case outrocaso:
            print(cons.MSG_OPCAO_INVALIDA)
            f.AguardaeLimpa()