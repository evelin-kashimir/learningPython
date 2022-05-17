from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Categoria, Item

class FormCategoria(ModelForm):
   #comunicação com o banco de dados - Metadados
    class Meta: 
        #tabela que sera trabalhada
        model = Categoria
        
        #campo que srão mostrados no front
        fields = ['id', 'nome']
        
        #apelido de tabela
        db_table = 'categoria'

class FormItem(ModelForm):
    class Meta:
        model = Item
        fields = ['id', 'descricao', 'categoria']
        db_table = 'item'