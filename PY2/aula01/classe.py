#instanciando uma classe 
class Veiculo:

    def __init__(self, modelo, ano, cor, qtdPortas, velMaxima, ligado = False):
        self.modelo = modelo
        self.ano = ano
        self.qtdPortas = qtdPortas
        self.cor = cor
        self.velMaxima = velMaxima
        self.ligado = ligado
        self.totalMarcha = 5
        self.marcha = 0
        self.velocidade = 0
        self.PodeMudarMarcha = False
        
    def ligar(self, ligar = True):
        if self.marcha == 0:
            if self.ligado:                    
                self.ligado = ligar
                self.PodeMudarMarcha = True
                return 'Vrum Vrum - Carro ligado!'
            return 'Carro já está ligado'
        return 'Opa - Carro não pode ser ligado, está engatado'

    def desligar(self):            
        if self.marcha == 0:
            if self.ligado:
                self.desligar = True
                self.PodeMudarMarcha = False
                return 'Carro desligado'           
            return 'Carro já estava desligado'
        return 'Carro não pode ser desligado fora do ponto morto'   
       
    def subirMarcha(self):
        if self.ligado and self.marcha <= self.totalMarcha:
            self.marcha+=1
            if self.marcha == 0:
                return 'Ponto morto'
            if self.marcha == -1:
                return 'Marcha Ré'
            else:
                return 'Subiu para: ' + str(self.marcha) + 'ª marcha!'
        return 'Já está na ' + str(self.marcha) + 'ª marcha!'

    def descerMarcha(self):
        if self.ligado and self.marcha > -1:
            self.marcha-=1
            if self.marcha == 0:
                return 'Ponto morto'
            if self.marcha == -1:
                return 'Marcha Ré'
            else:
                return 'Desceu para: ' + str(self.marcha) + 'ª marcha!'
        return 'Já está na ' + str(self.marcha) + 'ª marcha!'
       
    def acelerar(self):    
        if self.PodeMudarMarcha:
            self.velocidade += 20
            print(self.subirMarcha())
        
            return 'Velocidade atual: ' + str(self.velocidade)
        return 'O carro precisa estar ligado para acelerar.'

    def imprimeDados(self):
        print(self.modelo)
        print(self.ano)
        print(self.cor)
        print(self.qtdPortas)
        print(self.velMaxima)
        print(self.marcha)
        print(self.velocidade)








