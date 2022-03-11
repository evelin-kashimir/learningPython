num = int(input("Digite um valor inteiro: "))

for cont in range(num, 11):
    for valor in range(1,11):
        print(str(cont) + " x " + str(valor) +" = "+ str(valor*cont))


