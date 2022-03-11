nome = input("Digite o seu nome: ")

print("----- POSTO TAKARO ----- ")
print("[1] - ETANOL")
print("[2] - GASOLINA COMUM")
print("[3] - GASOLINA ADITIVADA")
print("[4] - DIESEL")
opcTipo = int(input("Informe o combustível desejado: "))

match opcTipo:
    case 1: 
        print("Forma de abastecimento: ")
        print("[1] - QUANTIDADE DE LITROS")
        print("[2] - VALOR EM R$")
        opcAbast = int(input("Digite: "))
        match opcAbast:
            case 1: 
                litros = float(input("Quantos litros: ")) 
                print("Total a pagar: " + str((litros * 4.689)))
            case 2:
                reais = float(input("Quanto deseja pagar: R$") )
                print("Total a de Litros: " + str((4.689 / reais )))
    case 2:
        print("Forma de abastecimento: ")
        print("[1] - QUANTIDADE DE LITROS")
        print("[2] - VALOR EM R$")
        opcAbast = int(input("Digite: "))
        match opcAbast:
                case 1: 
                    litros = float(input("Quantos litros: ")) 
                    print("Total a pagar: " + str((litros * 5.899)))
                case 2:
                    reais = float(input("Quanto deseja pagar: R$") )
                    print("Total a de Litros: " + str((5.899 / reais)))
    case 3:
        print("Forma de abastecimento: ")
        print("[1] - QUANTIDADE DE LITROS")
        print("[2] - VALOR EM R$")
        opcAbast = int(input("Digite: "))
        match opcAbast:
            case 1: 
                litros = float(input("Quantos litros: ")) 
                print("Total a pagar: " + str((litros * 7.099)))
            case 2:
                reais = float(input("Quanto deseja pagar: R$") )
                print("Total a de Litros: " + str((7.099 / reais )))
    case 4:
        print("Forma de abastecimento: ")
        print("[1] - QUANTIDADE DE LITROS")
        print("[2] - VALOR EM R$")
        opcAbast = int(input("Digite: "))
        match opcAbast:
            case 1: 
                litros = float(input("Quantos litros: ")) 
                print("Total a pagar: " + str((litros * 4.599)))
            case 2:
                reais = float(input("Quanto deseja pagar: R$"))
                print("Total a de Litros: " + str((4.599 / reais)))