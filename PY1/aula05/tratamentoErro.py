# TRATANDO ERROS - Exceções - Try Catch
try:                                                                                                              
    valor01 = int(input('Informe um valor inteiro: '))            
    valor02 = int(input('Informe outro valor inteiro: '))       
    print('A divisão dos valores digitados é: ' + str(valor01 / valor02)) 
    print('Obrigada por usar nosso sistema')  
except NameError:                                   #se a variavel não foi declarada nameError, lança uma exceção (variavel não existente globalmente)
    print('Alguma variável não existe')      
except ZeroDivisionError:                           #se o dividendo for 0, ZeroDivisionError lança uma exceção
    print('Impossível dividir por zero')                                                           
except ValueError:                                  #se o dado for inválido, valueError imprime uma exceção de valor incorreto
    print('Erro ao informar um dos valores ')   
except TypeError:
    print('Tipo de dado inválido')                  #Tipo de dado incorreto, exemplo string quando precisa ser inteiro, typeError lança uma exceção
except:
   print('Erro ao efetuar a divisão')               #se a divisão não ocorrer, imprima (tratamento genérico)

