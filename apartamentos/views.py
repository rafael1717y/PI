from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def index(request):    
    apartamentos = {
        1: 'Apartamento do João',
        2: 'Apartamento da Maria',
        3: 'Apartamento do José',
        4: 'Apartamento da Si'
    }

    dados = {
        'nome_dos_apartamentos': apartamentos
    }

    return render(request, 'index.html', dados)


def apartamento(request):
    return render(request, 'apartamento.html')

