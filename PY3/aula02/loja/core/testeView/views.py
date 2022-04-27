from email.policy import HTTP
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def retornaRequest(self):
    msg = 'Olá mundo'
    return HttpResponse(msg)

def exibeTabela(self):
    tabela =  '<table border="2">'
    tabela += '     <thead>'
    tabela += '         <tr>'
    tabela += '             <th colspan="2">Cabeçalho</th>'
    tabela += '         </tr>'
    tabela += '    </thead>'
    tabela += '    <tbody>'
    tabela += '        <tr>'
    tabela += '            <td>Item 1</td><td>Item 2</td>'
    tabela += '        </tr>'
    tabela += '    </tbody>'
    tabela += '    <tfoot>'
    tabela += '        <tr>'
    tabela += '            <td colspan="2" bgcolor = "#c3c3c3">Roda pé &nbsp;</td>'
    tabela += '        </tr>'
    tabela += '    </tfoot>'
    tabela += '</table>'
    return HttpResponse(tabela)

#renderizando a página html externa
def init(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def base(request):
    return render(request, 'base.html')