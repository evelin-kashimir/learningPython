def inserir(obj, item):
    gravaLog()
    return obj.append(item)

def ler(obj):
    gravaLog()
    for i in range(0, len(obj)):
        return print(obj(i))

def excluir(obj, item):
    return obj.remove(item)

def editar(obj, alterado, alterar):
    for x in range(0,len(obj)):
        if obj[x] == alterado:
            obj[x] = alterar

def gravaLog(opc):
    msg = ''
    match opc:
        case 1:
            msg = 'Item foi inserido!'
        case 2:
            msg = 'Item foi excluido'
        case 3:
            msg = 'Item foi Editado'
    try:
        arq = open('log.txt','a') #leitura
        arq.write(msg)
        arq.close()
    except FileNotFoundError:
        arq = open('log.txt','w') #leitura e sobrescrita
        arq.write(msg)
        arq.close()


