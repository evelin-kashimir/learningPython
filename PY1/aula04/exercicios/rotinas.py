def inserir(lista, item):
    if item in lista:
        return print("Não é possível inserir itens duplicados, esse item já existe.")
    else:
        lista.append(item)
        return print('Item adicionado com sucesso!')

def alterar(lista, alterado, paraAlterar):
    if alterado in lista:
        for x in range(0, len(lista)):
            if lista[x] == alterado:
                lista[x] = paraAlterar    
        return print('Valor alterado com sucesso!')
    else:
        return print(str(alterado) + ' não está cadastrado, impossível alterar!')

def visualizar(lista):
    for x in range(0,len(lista)):
        print(str(x+1) + ' - ' + lista[x])

def excluir(lista, excluido):
    if excluido in lista:
        lista.remove(excluido)
        return print('Item excluído com sucesso!')
    else:
        return print('Item inexistente, digite outro')
    
