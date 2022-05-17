
from django.shortcuts import redirect, render
from Item.form import FormCategoria, FormItem
from Item.models import Item, Categoria

# Create your views here.
def lista_categorias(request):
    categoria = Categoria.objects.all()
    total = categoria.count()
    return render(request, 'lista_categorias.html', {'categoria': categoria, 'total': total})

def cadastra_categoria(request):
    form = FormCategoria(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_categorias)
    return render(request, 'cadastra_categoria.html')

def altera_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    form = FormCategoria(request.POST, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect(lista_categorias)
    return render(request, 'altera_categoria.html', {'categoria': categoria})

def exclui_categoria(request):
    return render(request, 'exclui_categoria.html')


def lista_itens(request):
    item = Item.objects.all()
    total = item.count()
    return render(request, 'lista_itens.html', {'item': item, 'total': total})

def cadastra_item(request):
    categoria = Categoria.objects.all()
    form = FormItem(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_itens)
    return render(request, 'cadastra_item.html', {'categoria': categoria})

def altera_item(request,id):
    item = Item.objects.get(id=id)
    categoria = Categoria.objects.all()
    tipoCategoria = Categoria.objects.get(id=item.categoria_id)
    form = FormItem(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect(lista_itens)
    return render(request, 'altera_item.html', {'item': item, 'categoria': categoria, 'tipoCategoria': tipoCategoria.id})

def exclui_item(request):
    return render(request, 'exclui_item.html')
