nome = input('Digite seu nome: ')
nascimento = int(input('Digite o seu ano de nascimento: '))

anoAtual = 2022
idadeMinima = 18
idade = anoAtual - nascimento

if(idade > idadeMinima):
    print(nome + ", você tem " + str(idade) + " anos, ESTÁ apto(a) a dirigir!")
else:
    faltam = idadeMinima - idade
    print(nome + ", você tem " + str(idade) + " anos, NÃO ESTÁ apto(a) a dirigir! Faltam mais " + str(faltam) + " anos.")


