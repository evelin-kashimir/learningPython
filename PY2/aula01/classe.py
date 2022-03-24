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
        self.totalMarcha = 5
        self.marcha = 0

    def ligar(self, ligar = True):
        self.ligado = ligar
        if self.ligado:
            return 'Vrum Vrum - Carro já está ligado!'
        return 'Opa - Carro desligado, vamos ligar!'

    def desligar(self):
        if self.ligado:
            self.desligar = True
            return 'Carro desligado'
        return 'Carro já está desligado'   

    def subirMarcha(self):
        if self.ligado and self.marcha <= self.totalMarcha:
            self.marcha+=1
            if self.marcha == 0:
                return 'Ponto morto'
            if self.marcha == -1:
                return 'Marcha Ré'
            else:
                return 'Subiu para: ' + str(self.marcha) + 'ª marcha!'

    def descerMarcha(self):
        if self.ligado and self.marcha > -1:
            self.marcha-=1
            if self.marcha == 0:
                return 'Ponto morto'
            if self.marcha == -1:
                return 'Marcha Ré'
            else:
                return 'Desceu para: ' + str(self.marcha) + 'ª marcha!'
         
    def imprimeDados(self):
        print(self.modelo)
        print(self.ano)
        print(self.cor)
        print(self.qtdPortas)
        print(self.velMaxima)
        print(self.marcha)







