from django.db import models
from datetime import datetime
from pessoas.models import Pessoa


class Apartamento(models.Model):
    #pessoa é o cadastrador de um imóvel do condomínio
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_apartamento = models.CharField(max_length=200)
    nome_proprietario = models.CharField(max_length=200)
    cpf_proprietario = models.CharField(max_length=14, null=False, blank=False, unique=True)
    descricao_apartamento = models.TextField()
    categoria = models.CharField(max_length=100)  # aluguel, venda e aluguel/venda
    valor_aluguel = models.DecimalField(max_digits=15, decimal_places=2, blank=True)  ## se nao cadastrar deixa em bco 
    valor_venda = models.DecimalField(max_digits=15, decimal_places=2, blank=True) 
    email_proprietario = models.EmailField(default='', max_length=200, verbose_name='Email')
    fone_proprietario = models.IntegerField(blank=True, verbose_name='Número de telefone')
    data_criacao = models.DateTimeField(default=datetime.now, blank=True)
    ultima_edicao = models.DateTimeField(auto_now_add=False, auto_now=True)
    # não deixar visível qdo se cadastrar um novo apto
    apartamento_publicado = models.BooleanField(default=False)
    # inclusão de um imagem para cada apto
    foto_apartamento = models.ImageField(upload_to = 'fotos/%d/%m/%Y/', blank=True)








