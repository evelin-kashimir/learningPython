from dataclasses import field, fields
from django.forms import ModelForm
from .models import TpPessoa, Cliente, Fornecedor, Usuarios

class FormTpPessoa(ModelForm):
    class Meta:
        model = TpPessoa
        fields = ['id', 'descricao']
        db_table = 'TpPessoa'

class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'CpfCnpj', 'email', 'tp_pessoa']
        db_table = 'cliente'

class FormFornecedor(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'fantasia', 'email', 'CpfCnpj', 'tp_pessoa']
        db_table = 'fornecedor'

class FormUsuario(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['id', 'nome', 'login', 'senha']
        db_table = 'usuario'