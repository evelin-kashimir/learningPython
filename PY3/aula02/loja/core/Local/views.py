from django.shortcuts import redirect, render
from Local.form import FormCidade, FormEstado
from Local.models import Cidade, Estado

# Create your views here.
def lista_estados(request):
    #pegando todos os dados do formulário para passao ao banco através dos módulos
    estado = Estado.objects.all()               #chamando o dicionario (objeto)
    total = estado.count()
    return render(request, 'lista_estados.html', {'estado': estado, 'total': total})

def cadastra_estado(request):
    form = FormEstado(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_estados)
    return render(request, 'cadastra_estado.html')

def altera_estado(request,id):
    estado = Estado.objects.get(id=id)
    form = FormEstado(request.POST, instance=estado)
    if form.is_valid():
        form.save()
        return redirect(lista_estados)
    return render(request, 'altera_estado.html', {'estado': estado})

def exclui_estado(request):
    return render(request, 'exclui_estado.html')


def lista_cidades(request): 
    cidade = Cidade.objects.all()
    total = cidade.count()
    return render(request, 'lista_cidades.html', {'cidade': cidade, 'total': total})

def cadastra_cidade(request):
    estado = Estado.objects.all()
    form = FormCidade(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_cidades)
    return render(request, 'cadastra_cidade.html', {'estados': estado})

def altera_cidade(request, id):
    cidade = Cidade.objects.get(id=id)
    sigla = Estado.objects.all()
    siglaEstado = Estado.objects.get(id=cidade.sigla_id)
    form = FormCidade(request.POST, instance=cidade)
    if form.is_valid():
        form.save()
        return redirect(lista_cidades)
    return render(request, 'altera_cidade.html',{'cidade': cidade, 'sigla': sigla, 'siglaEstado': siglaEstado} )
    
def exclui_cidade(request):
    return render(request, 'exclui_cidade.html')



