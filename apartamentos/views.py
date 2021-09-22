from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponse
from .models import Apartamento

# Create your views here.

def index(request):    
    # filtro para editar os apartamentos antes de publicá-los e ordenando pelos aptos cadastrados recentemente
    apartamentos = Apartamento.objects.order_by('-data_criacao').filter(apartamento_publicado = True)
       
    dados = {
        'apartamentos': apartamentos
    }
    return render(request, 'index.html', dados)


def apartamento(request, apartamento_id):
    apartamento = get_object_or_404(Apartamento, pk=apartamento_id)  #primary key
    
    apartamento_a_exibir = {
        'apartamento' : apartamento
    }
    return render(request, 'apartamento.html', apartamento_a_exibir)


def buscar(request):
    lista_apartamentos = Apartamento.objects.order_by('-data_criacao').filter(apartamento_publicado = True)
    if 'buscar' in request.GET:
        ### ou categoria a buscar ??
        nome_a_buscar = request.GET['buscar']   
        if buscar:
            lista_apartamentos = lista_apartamentos.filter(nome_apartamento__icontains=nome_a_buscar)

    dados = {
        'apartamentos' : lista_apartamentos
    }

    return render(request, 'buscar.html', dados)

