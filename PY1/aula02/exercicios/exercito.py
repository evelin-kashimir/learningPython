print("-*-*- EXÉRCITO BRASILEIRO -*-*- ")
sexo = input("Seu sexo: [ M ] [ F ]")

#transforma a string em uppercase
match sexo.upper():
    case 'M' :
        nome = input("Digite o seu nome: ")
        idade = int(input("Sua idade: "))
        match idade:
            case 18:
                print("Inscrição concluída!")
                print("Nome: " + nome)
                print("Idade: " + str(idade))
                print("Sexo: " + sexo)
                print("Função: Soldado")   
            case menor:
                 print("Sendo menor de idade, não se pode entrar no exercito")
    case 'F':
        nome = input("Digite o seu nome: ")
        print(nome + ", Infelizmente no ano atual, não aceitamos mulheres para serem soldadas.")

     
