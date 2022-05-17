from http import client
from itertools import count
from pydoc import cli
from django.shortcuts import redirect, render
from Pessoa.form import FormCliente, FormFornecedor,FormTpPessoa, FormUsuario
from Pessoa.models import Cliente, Fornecedor, TpPessoa, Usuarios


#mandando as def's para o html
def lista_tp_pessoas(request):
    tipoPessoa = TpPessoa.objects.all()
    total = tipoPessoa.count() #contador para trazer quantos registros existem na tabela
    return render(request, 'lista_tp_pessoa.html', {'tipos': tipoPessoa, 'total': total})

def cadastra_tp_pessoa(request):
    #logica para salvar os dados no banco
    form = FormTpPessoa(request.POST or None) 
    if form.is_valid():
        form.save()
        return redirect(lista_tp_pessoas)
    return render(request, 'cadastra_tp_pessoa.html')

def altera_tp_pessoa(request, id):
    tipo = TpPessoa.objects.get(id=id) #pegando o campo para alteração e setando o mesmo id para fazer o update. 
    form = FormTpPessoa(request.POST, instance=tipo) #vai alterar somente o que foi citado no instance
    if form.is_valid():
        form.save()
        return redirect(lista_tp_pessoas)
    return render(request, 'altera_tp_pessoa.html', {'tipo': tipo})

def exclui_tp_pessoa(request):
    return render(request, 'exclui_tp_pessoa.html')


def lista_clientes(request):
    cliente = Cliente.objects.all()
    total = cliente.count()
    return render(request, 'lista_cliente.html', {'cliente' : cliente, 'total': total})

def cadastra_cliente(request):
    tipo = TpPessoa.objects.all() #select 
    form = FormCliente(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_clientes)
    return render(request, 'cadastra_cliente.html', { "tipo": tipo } )

def altera_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    tipo = TpPessoa.objects.all()
    tipoCliente = TpPessoa.objects.get(id=cliente.tp_pessoa_id) #pegando o id do tipo de pessoa, para trazer já selecionado na alteração
    form = FormCliente(request.POST, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect(lista_clientes)
    return render(request, 'altera_cliente.html', {'cliente': cliente, 'tipo': tipo, 'tipoPessoa': tipoCliente.id}) 

def exclui_cliente(request):
    return render(request, 'exclui_cliente.html')


def lista_fornecedores(request):
    fornecedor = Fornecedor.objects.all()
    total = fornecedor.count()
    return render(request, 'lista_fornecedores.html', {'fornecedor': fornecedor, 'total': total})

def cadastra_fornecedor(request):
    tipo = TpPessoa.objects.all()
    form = FormFornecedor(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_fornecedores)
    return render(request, 'cadastra_fornecedor.html', { "tipo": tipo })
   
def altera_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    tipo = TpPessoa.objects.all()
    tipoFornecedor = TpPessoa.objects.get(id=fornecedor.tp_pessoa_id)
    form = FormFornecedor(request.POST, instance=fornecedor)
    if form.is_valid():
        form.save()
        return redirect(lista_fornecedores)
    return render(request, 'altera_fornecedor.html', {'fornecedor': fornecedor, 'tipo': tipo, 'tipoPessoa': tipoFornecedor.id})

def exclui_fornecedor(request):
    return render(request, 'exclui_fornecedor.html')


def lista_usuarios(request):
    usuario = Usuarios.objects.all()
    total = usuario.count()
    return render(request, 'lista_usuarios.html', {'usuario': usuario, 'total': total})

def cadastra_usuario(request):
    form = FormUsuario(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_usuarios)
    return render(request, 'cadastra_usuario.html')
   
def altera_usuario(request, id):
    usuario = Usuarios.objects.get(id=id)
    form = FormUsuario(request.POST, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect(lista_usuarios)
    return render(request, 'altera_usuario.html', {'usuario': usuario})

def exclui_usuario(request):
    return render(request, 'exclui_usuario.html')

