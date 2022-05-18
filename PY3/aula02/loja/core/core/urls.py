"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from mimetypes import init
from django.contrib import admin
from django.urls import path
from testeView.views import exibeTabela, retornaRequest, init, contato, base

from Pessoa.views import lista_clientes, lista_fornecedores, lista_tp_pessoas, lista_usuarios
from Pessoa.views import cadastra_cliente, cadastra_fornecedor, cadastra_tp_pessoa, cadastra_usuario
from Pessoa.views import altera_cliente, altera_fornecedor, altera_tp_pessoa, altera_usuario
from Pessoa.views import exclui_cliente, exclui_fornecedor, exclui_tp_pessoa, exclui_usuario

from Item.views import lista_categorias, lista_itens
from Item.views import cadastra_categoria, cadastra_item
from Item.views import altera_categoria, altera_item
from Item.views import exclui_categoria, exclui_item

from Local.views import lista_estados, lista_cidades
from Local.views import cadastra_cidade, cadastra_estado
from Local.views import altera_cidade, altera_estado
from Local.views import exclui_cidade, exclui_estado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exemplo', retornaRequest),
    path('tabela', exibeTabela),
    path('init', init, name='init'),
    path('contato', contato, name='contato'),
    path('base', base),
    path('', init),

    #Pessoa
    path('tipos-pessoa', lista_tp_pessoas, name='lista-tipos-pessoa'), #setando um name para tratar erro de concatenação na barra da url
    path('clientes', lista_clientes, name='clientes'),
    path('fornecedores', lista_fornecedores, name='fornecedores'),
    path('usuarios', lista_usuarios, name='usuarios'),

    path('cadastra-tipo-pessoa', cadastra_tp_pessoa, name='cadastra-tipo-pessoa'),
    path('cadastra-cliente', cadastra_cliente, name='cadastra-cliente'),
    path('cadastra-fornecedor', cadastra_fornecedor, name='cadastra-fornecedor'),
    path('cadastra-usuario', cadastra_usuario, name='cadastra-usuario'),

    path('altera-tipo-pessoa/<int:id>', altera_tp_pessoa),
    path('altera-cliente/<int:id>', altera_cliente),
    path('altera-fornecedor/<int:id>', altera_fornecedor),
    path('altera-usuario/<int:id>', altera_usuario),

    path('exclui-tipo-pessoa/<int:id>', exclui_tp_pessoa),
    path('exclui-cliente/<int:id>', exclui_cliente),
    path('exclui-fornecedor/<int:id>', exclui_fornecedor),
    path('exclui-usuario/<int:id>', exclui_usuario),

    
    #Item
    path('categorias', lista_categorias, name='categorias'),
    path('itens', lista_itens, name='itens'),

    path('cadastra-item', cadastra_item, name='cadastra-item'),
    path('cadastra-categoria', cadastra_categoria, name='cadastra-categoria'),

    path('altera-categoria/<int:id>', altera_categoria),
    path('altera-item/<int:id>', altera_item),
   
    path('exclui-categoria/<int:id>', exclui_categoria),
    path('exclui-item/<int:id>', exclui_item),


    #Local
    path('estados', lista_estados, name='estados'),
    path('cidades', lista_cidades, name='cidades'),

    path('cadastra-estado', cadastra_estado, name='cadastra-estado'),
    path('cadastra-cidade', cadastra_cidade, name='cadastra-cidade'),

    path('altera-estado/<int:id>', altera_estado),
    path('altera-cidade/<int:id>', altera_cidade),

    path('exclui-estado/<int:id>', exclui_estado),
    path('exclui-cidade/<int:id>', exclui_cidade)
]; 


