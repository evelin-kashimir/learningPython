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
from Item.views import lista_categorias, lista_itens
from Local.views import lista_estados, lista_cidades

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exemplo', retornaRequest),
    path('tabela', exibeTabela),
    path('init', init),
    path('contato', contato),
    path('base', base),
    path('', init),
    path('tipos-pessoa', lista_tp_pessoas ),
    path('clientes', lista_clientes),
    path('fornecedores', lista_fornecedores),
    path('usuarios', lista_usuarios),
    path('categorias', lista_categorias),
    path('itens', lista_itens),
    path('estados', lista_estados),
    path('cidades', lista_cidades)
]; 


