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
