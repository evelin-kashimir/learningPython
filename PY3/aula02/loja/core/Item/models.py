from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True, blank=False)

    class Meta:
        db_table = 'Categoria'

    def __str__(self):
        return self.nome

class Item(models.Model):
    descricao = models.CharField(max_length=100, unique= True, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Item'

    def __str__(self):
        return self.descricao


