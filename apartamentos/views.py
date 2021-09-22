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


