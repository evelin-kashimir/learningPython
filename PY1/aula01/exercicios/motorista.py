nome = input('Digite seu nome: ')
nascimento = int(input('Digite o seu ano de nascimento: '))

anoAtual = 2022
idade = anoAtual - nascimento

if(idade > 18):
    print(nome + ", você tem " + str(idade) + " anos, ESTÁ apto(a) a dirigir!")
else:
    print(nome + ", você tem " + str(idade) + " anos, NÃO ESTÁ apto(a) a dirigir!")

