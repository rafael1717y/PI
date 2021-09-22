from os import name
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:apartamento_id>', views.apartamento, name='apartamento'),
    path('busca', views.buscar, name = 'buscar')

]