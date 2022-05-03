from django.http import HttpResponse
from django.shortcuts import render

#mandando as def's para o html
def lista_tp_pessoas(request):
    return render(request, 'lista_tp_pessoa.html')

def lista_clientes(request):
    return render(request, 'lista_cliente.html')

def lista_fornecedores(request):
    return render(request, 'lista_fornecedores.html')

def lista_usuarios(request):
    return render(request, 'lista_usuarios.html')
