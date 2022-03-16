nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0  
nota1 = 0
saque = int(input("Valor de Saque: R$"))

#notas 100
while( saque >= 100 ):
    nota100+=1
    saque -= 100

#notas 50
while( saque >= 50 ):
    nota50+=1
    saque -= 50

#notas 20
while( saque >= 20 ):
    nota20+=1
    saque -= 20

#notas 10
while( saque >= 10 ):
    nota10+=1
    saque -= 10

#notas 5
while( saque >= 5):
    nota5+=1
    saque -= 5

#notas 2
while( saque >= 2):
    nota2+=1
    saque -= 2

#notas 1
while( saque >= 1 ):
    nota1+=1
    saque -= 1

print("Notas de 100 -> " + str(nota100))
print("Notas de 50 -> " + str(nota50))
print("Notas de 20 -> " + str(nota20))
print("Notas de 10 -> " + str(nota10))
print("Notas de 5 -> " + str(nota5))
print("Notas de 2 -> " + str(nota2))
print("Notas de 1 -> " + str(nota1))
