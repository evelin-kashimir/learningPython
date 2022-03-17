#importando módulos
import os
import time
#funções podem ser declaradas em outro arquivo, facilitando a padronização do software

#declarando uma subRotina - função 
def mensagem(pValor):
    print(pValor)

def segundaMensagem():
    print('Seja bem vindo(a)!')

def soma(num1, num2 = 0): #setando valor default
    print('Soma: ' + str(num1 + num2))


#chamando as funções
mensagem('Adoro programar em Python')
segundaMensagem()
soma(7,3)


num1 = int(input("Informe um numero inteiro: "))
num2 = int(input("Informe outro numero inteiro: "))

soma(num1, num2)
soma(num1)

#quando utilizar o return, para imprimir deve se usar o print obrigatoriamente
def par(valor):
    def validaResultado(opc):
        if type(opc) == int:
            return 'Valor é valido'
        return 'Valor é invalido'

    if valor % 2 == 0:
        print(validaResultado(1))
        return True
    print(validaResultado(2))
    return False


#o return que é retornado, sempre é o primeiro que passa no teste de true
def minhaFuncao():
    return 1
    return 2
    return 3
    return 4

if par(2):
    print('é par')
else:
    print('é impar')
