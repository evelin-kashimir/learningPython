#importando a classe Veiculo
from classe import Veiculo

#instanciando o objeto c1
carro = Veiculo('Corsa', 2000, 'preto', 4, 200, True) #self - objeto que está sendo criado 
carro.imprimeDados()
print(carro.ligar())
print(carro.subirMarcha())
print(carro.subirMarcha())
print(carro.subirMarcha())
print(carro.subirMarcha())
carro.imprimeDados()
print(carro.descerMarcha())

carro02 = Veiculo('Porshe', 2022, 'preto', 2, 260)
carro02.imprimeDados()
print(carro02.ligar())
print(carro02.subirMarcha())
print(carro02.subirMarcha())
print(carro02.subirMarcha())
print(carro02.subirMarcha())
print(carro02.subirMarcha())
print(carro02.descerMarcha())
carro.imprimeDados()


