from django.contrib import admin
from .models import Apartamento

class ListandoApartamentos(admin.ModelAdmin):
    list_display = ('id', 'nome_apartamento', 'categoria', 'valor_aluguel', 'valor_venda', 'apartamento_publicado')
    list_display_links = ('id', 'nome_apartamento')
    search_fields = ('nome_apartamento',)
    list_filter = ('categoria',)
    list_per_page = 3  # lista nr de páginas
    list_editable = ('apartamento_publicado',)



admin.site.register(Apartamento, ListandoApartamentos)

