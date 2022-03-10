print("Bem vindo(a) a segunda aula de Python Fundamentos!")

op = int(input("Opção desejada: "))
match op:
    case 1:
        print("Primeira Opção")
    case 2:
        print("Segunda Opção")
    case 3:
        print("Terceira Opção")
    case 4:
        print("Quarta Opção")
    case default:
        print("Opção inválida")
        