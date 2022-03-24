#instanciando uma classe 
class Veiculo:
    ''' 
    Atributos
    modelo = 'Porshe'
    ano = 2022
    cor = 'preto'
    qtdPortas = 4
    velMaxima = 260
    '''
    #Método construtor - Atributos de instancia
    def __init__(self, modelo, ano, cor, qtdPortas, velMaxima, ligado = False):
        self.modelo = modelo
        self.ano = ano
        self.qtdPortas = qtdPortas
        self.cor = cor
        self.velMaxima = velMaxima
        self.ligado = ligado

    def ligar(self, ligar = True):
        self.ligado = ligar
        if self.ligado == True:
            print('Vrum Vrum - Carro ligado!')
        else:
            print('Opa - Carro desligado!')

#instanciando o objeto c1
carro = Veiculo('Corsa', 2000, 'preto', 4, 200, True) #self - objeto que está sendo criado 
print(carro.modelo)
print(carro.cor)
print(carro.ano)
print(carro.qtdPortas)
print(carro.velMaxima)
carro.ligar()

carro02 = Veiculo('Porshe', 2022, 'preto', 2, 260)
print(carro02.modelo)
print(carro02.cor)
print(carro02.ano)
print(carro02.qtdPortas)
print(carro02.velMaxima)
print(carro02.ligado)
carro02.ligar(False)







