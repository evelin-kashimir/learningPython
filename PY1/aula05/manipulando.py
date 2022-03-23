from genericpath import exists

#se existe o arquivo no diretório, abra para leitura, se não 
if exists('arquivo.txt'):
    arq = open('arquivo.txt','r')
    arq.close() #fechando o arquivo 
else:
    print('Arquivo não existe')

try:
    arq = open('arquivo.txt','r') #leitura
    arq.close()
    print('Arquivo foi aberto para leitura e está fechado.')
except FileNotFoundError:
    print('O arquivo não existe e será criado')
    arq = open('arquivo.txt','w') #leitura e sobrescrita
    arq.close()
except:
    print('Ocorreu algum erro ao tentar abrir o arquivo')

try:
    arq = open('arquivo.txt', 'w')
    arq.write('Olá Mundo!\n') #escrevendo no arquivo
    arq.close()
except:
    print('Ocorreu algum erro ao tentar escrever no arquivo')

try:
    arq = open('arquivo.txt', 'a') #adiciona o novo texto após a ultima atualização
    arq.write('Seja bem vindo(a) à manipulação de arquivos')
    arq.close()
except:
    print('Erro ao tentar escrever no arquivo')

try:
    arq = open('arquivo.txt', 'r')
    conteudo = arq.read()   #lê o arquivo e imprime na tela
    print(conteudo)
    arq.close()
except:
    print('Erro ao abrir o arquivo para leitura')