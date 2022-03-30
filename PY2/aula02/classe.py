#herança 
class Mamifero():
    
    #construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.parado = True
    
    #métodos
    def mover(self):
        print(self.nome + ' é ' + __class__.__name__ + ' está se movendo...')
        self.parado = False
    
    def parar(self):
        print(self.nome + ' é ' + __class__.__name__ + ' parou!')
        self.parado = True

    def comer(self):
            #pegando o nome da classe que o método está implementado
        print(self.nome + ' é ' + __class__.__name__ + ' está comendo...')

#instanciando a classe
ser = Mamifero('Cachorro', 20)
ser.mover()
ser.parar()
ser.comer()

#herdando metodos da classe mãe (dentro do parenteses)
class Cao(Mamifero):

    #método construtor próprio
    def __init__(self, nome):
        self.nome = nome

    def latir(self):
        print(self.nome + ' é ' + __class__.__name__ + ' e está latindo...')

cao = Cao('Olavo')
cao.mover()
cao.parar()
cao.comer()
cao.latir()

#herdando metodos e atributos da classe mãe (dentro do parenteses)
class Pessoa(Mamifero):
    def falar(self):
        print(self.nome + ' é ' + __class__.__name__ + ' está falando...')

pessoa = Pessoa('Mariana', 25)
pessoa.comer()
pessoa.falar()