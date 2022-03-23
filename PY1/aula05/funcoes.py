def soma(obj):
    total = 0
    for cont in range(0, len(obj)):
        total+= obj[cont]
    return print(total)

def divisao(obj):
    num1 = 0
    num2 = 0
    for cont in range(0, len(obj)):
        if cont == 0:
            num1 = obj[cont]
        if cont == 1:
            num2 = obj[cont]
            break
    try:
        return print(num1 / num2)
    except ZeroDivisionError:
        return print('Não é possível dividir por zero')
        
def defineOpc(obj, opc):
    match opc:
        case 1:
            soma(obj)
        case 2:
            divisao(obj)
        case outroCaso:
            return 'Opção inválida'
