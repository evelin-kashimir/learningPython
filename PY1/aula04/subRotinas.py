#funções podem ser declaradas em outro arquivo, facilitando a padronização do software

#declarando uma subRotina - função 
def mensagem(pValor):
    print(pValor)

def segundaMensagem():
    print('Seja bem vindo(a)!')

def soma(num1, num2):
    print('Soma: ' + str(num1 + num2))

#chamando as funções
mensagem('Adoro programar em Python')
segundaMensagem()
soma(7,3)

