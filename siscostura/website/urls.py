# Importamos a função index() definida no arquivo views.py
from django.urls import path
from django.urls import include
from . import views

app_name = 'website'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [

    # GET /
    path('', views.HomeView.as_view(), name="index"),

    # GET /clientes
    path('clientes/', views.HomeClienteView.as_view(),
         name="index_clientes"),

    # GET /clientes/cadastrar
    path('clientes/cadastrar', views.CriaClienteView.as_view(),
         name="cadastra_cliente"),

    # GET /clientes
    path('clientes/lista', views.ListaclientesView.as_view(),
         name="lista_clientes"),

    # GET/POST /clientes/{pk}
    path('clientes/<pk>', views.AtualizaClienteView.as_view(),
         name="atualiza_cliente"),

    # GET/POST /clientes/excluir/{pk}
    path('clientes/excluir/<pk>',
         views.DeletaClienteView.as_view(), name="deleta_cliente"),


]
