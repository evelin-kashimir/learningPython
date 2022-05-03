from django.shortcuts import render

# Create your views here.
def lista_categorias(request):
    return render(request, 'lista_categorias.html')

def lista_itens(request):
    return render(request, 'lista_itens.html')

