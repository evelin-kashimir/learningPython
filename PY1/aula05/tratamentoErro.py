# TRATANDO ERROS - Exceções
try:                                                            # 1 - tente efetuar a divisão   
    try:                                                        # 2 - tente receber o primeiro dado
        valor01 = int(input('Informe um valor inteiro: '))     
        try:
            valor02 = int(input('Informe outro valor inteiro: '))   # 3 -tente receber o segundo valor
            try:
                print('A divisão dos valores digitados é: ' + str(valor01 / valor02)) # 4 -tente dividir os valores
                print('Obrigada por usar nosso sistema')        
            except:                                             
                print('Impossível dividir por zero')            # 4 - se o dividendo for 0, imprima
        except:
            print('Erro ao informar o segundo valor')           # 2 - se der erro segundo valor, imprima 
    except:
        print('Erro ao informar o primeiro valor ')             # 3 - se der erro no primeiro valor, imprima
except:
    print('Erro ao efetuar a divisão')                          # 1 - se a divisão não ocorrer, imprima

