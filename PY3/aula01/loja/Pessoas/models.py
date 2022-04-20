import email
from django.db import models

#criando tabela em banco de dados através do django
class CPFCNPJ(models.Model):
    numero = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.numero

class Cliente(models.Model):
    #criando campos da tabela cliente
    nome = models.CharField(max_length=50)      #varchar, tamanho maximo 50
    email = models.EmailField(max_length=100, blank=True)   #tipo email, tamanho máximo 100
    fone = models.CharField(max_length=11) 
    
    #criando relacionamento entre as tabelas, tabela referencia (CPFCNPJ), Cascade = não deixara excluir se estiver atrelado a outra tabela 
    cpf_cnpj = models.OneToOneField(CPFCNPJ,on_delete=models.CASCADE) #um para um 
    
    #printando na tela dodjango as informações do banco
    def __str__(self):
        return 'Nome: ' + self.nome + ' | E-mail: ' + str(self.email) +  ' | Fone: ' + self.fone +  ' | CPF/CNPJ: ' + str(self.cpf_cnpj)

    #renomeando a tabela
    class Meta:
        db_table = 'Cliente'
