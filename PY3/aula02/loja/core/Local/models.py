from django.db import models

# Create your models here.
class Estado(models.Model):
    sigla = models.CharField(max_length=2, unique=True, blank=False)
    nome = models.CharField(max_length=50, unique=True, blank=False)

    class Meta:
        db_table: 'Estado'

    def __str__(self):
        return self.sigla + ' '
    
    def __str__(self):
        return self.nome

class Cidade(models.Model): 
    nome = models.CharField(max_length=50, unique=True, blank=False)
    sigla = models.ForeignKey(Estado, on_delete=models.CASCADE)

    class Meta:
        db_table: 'Cidade'

    def __str__(self):
        return self.nome 
    