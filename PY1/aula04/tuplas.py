#tuplas - listas não iteráveis e imutáveis 
dia_semana = ('Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado' )
compras = ['pão', 'açucar','leite']
comprasVerdura = ['cenoura', 'alface','pepino']
print(type(dia_semana))
print((dia_semana))
for x in range(0,len(dia_semana)):
    print(dia_semana[x].replace('-Feira', '')) #refatorando os indices, alterando o conteudo, pelo outro especificados nos parametros

pessoas = ('joão', 'maria', 'josé', 'joão', 'pedro', 'ana', compras, comprasVerdura)
print(pessoas.count('joão')) #contando quantos valores tem daquele especificado

total = 0
for x in range(0,len(pessoas)):
    if type(pessoas[x]) is list:
        total += 1
print('Total de listas: ' + str(total))
