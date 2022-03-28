#importando a classe Veiculo
from classe import Veiculo

#instanciando o objeto c1
carro = Veiculo('Corsa', 2000, 'preto', 4, 200, True) #self - objeto que está sendo criado 
print(carro.ligar())
print(carro.acelerar())
print(carro.subirMarcha())

print(carro.descerMarcha())
print(carro.desligar())



