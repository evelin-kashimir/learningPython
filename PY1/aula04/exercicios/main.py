from rotinas import inserir, excluir, visualizar, alterar
import os
import time

lista = []
opc = 5

while(opc != 0):
    print("".rjust(40, "-"))
    print("MENU PRINCIPAL".center(40, " "))
    print("".ljust(40, "-"))
    print("[1] - CADASTRAR ")
    print("[2] - ALTERAR ")
    print("[3] - VISUALIZAR ")
    print("[4] - EXCLUIR ")
    print("[0] - SAIR ")
    print("".rjust(40, "-"))

    opc = int(input('->'))
    match opc:
        case 1: 
            os.system('cls')
            print("".rjust(40, "-"))
            print("CADASTRO".center(40, " "))
            print("".ljust(40, "-"))
            item = input("Produto: ")
            inserir(lista, item)
        case 2:
            os.system('cls')
            print("".rjust(40, "-"))
            print("ALTERAR ITEM".center(40, " "))
            print("".ljust(40, "-"))
            alterado = input("Digite o produdo que deseja alterar: ")
            paraAlterar = input("Digite o novo valor: ")
            alterar(lista, alterado, paraAlterar)
        case 3:
            os.system('cls')
            print("".rjust(40, "-"))
            print("LISTA".center(40, " "))
            print("".ljust(40, "-"))
            visualizar(lista)
        case 4:
            os.system('cls')
            print("".rjust(40, "-"))
            print("EXCLUIR ITEM".center(40, " "))
            print("".ljust(40, "-"))           
            excluido = input("Digite o produto que deseja remover: ")
            excluir(lista, excluido)
        case 0:
            os.system('cls')
            print("Saindo...")
        case outroCaso: 
            os.system('cls')
            print('Opção inválida! ')

    time.sleep(2)
    os.system('cls')


