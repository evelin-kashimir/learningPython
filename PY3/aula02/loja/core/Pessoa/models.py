from pyexpat import model
from django import db
from django.db import models

# Criando aplicações do banco de dados
class TpPessoa(models.Model):                                   
    descricao = models.CharField(max_length=50 , unique=True, blank=False) #tamanho, chave unica, not null

    class Meta:
        db_table='TipoDePessoa' #nome da tabela

    def __str__(self):
        return self.descricao   #nome do campo e o tipo

class Cliente(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    CpfCnpj = models.CharField(max_length=15, unique=True, blank=False)
    email = models.CharField(max_length=100, unique=True, blank=True)
    tp_pessoa = models.ForeignKey(TpPessoa, on_delete=models.CASCADE)

    class Meta:
        db_table='Cliente'

    def __str__(self):
        return self.nome
    
    def __str__(self):
        return self.CpfCnpj

class Fornecedor(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    fantasia = models.CharField(max_length=50, unique=True, blank=False)
    email = models.CharField(max_length=100, unique=True, blank=True)
    CpfCnpj = models.CharField(max_length=15, unique=True, blank=False)
    tp_pessoa = models.ForeignKey(TpPessoa, on_delete=models.CASCADE) #impede que o usuario exclua o id que estiver vinculado a outra tabela

    class Meta:
        db_table='Fornecedor'

    def __str__(self):
        return self.nome
    
    def __str__(self):
        return self.CpfCnpj

class Usuarios(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    login = models.CharField(max_length=50, unique=True, blank=False)
    senha = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table='Usuario'

    def __str__(self):
        return self.nome
    
    def __str__(self):
        return self.login

#PYTHON MANAGE.PY MAKEMIGRATIONS
#PYTHON MANAGE.PY MIGRATE
#DONE!  :)
