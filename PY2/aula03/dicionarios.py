# #Dicionarios = Chave e valor (Objetos)
# di = {}
# di['chave'] = 'valor'   #atribuindo valor ao dicionario
# print(di['chave'])      #'chave' = indice do dicionario

emails = {}
#adicionando itens ao dicionario
emails['juca'] = 'juca@gmail.com'
emails['pedro'] = 'pedro@gmail.com'
emails['ana'] = 'ana@gmail.com'
emails['codigo'] = 12345
emails[5] = True
emails['lista'] = [1, 2, 'três', 0.5, False]
print(emails)
print(emails['lista'][1])

#imprimindo todos os itens do dicionario
print(emails)

#imprimindo o email especifico do indice
print(emails['ana'])

#imprimindo todos os e-mails
for x in emails:
    print(emails[x]) #trás somente os valores

if 'Ana' in emails:
    print('existe')
    emails['Ana'] = 'EmailAtualizado@gmail.com'
else:
    print('não existe')
    emails['Ana'] = 'novoEmail@gmail.com'

#imprimindo todos os itens do dicionario
print(emails)

#removendo um item do dicionario
if 'anas' in emails: 
    emails.pop('anas')

try:
    emails.pop('anas')
except KeyError:
    print('Chave inexistente')


