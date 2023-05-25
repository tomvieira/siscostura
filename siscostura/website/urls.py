# Importamos a função index() definida no arquivo views.py
from django.urls import path
from django.urls import include
from . import views
from .views import delete_item

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


    # GET /pedidos
    path('pedidos/', views.HomePedidoView.as_view(),
         name="index_pedidos"),

    # GET /pedidos/cadastrar
    path('pedidos/cadastrar', views.CriaPedidoView.as_view(),
         name="cadastra_pedido"),

    # GET /pedidos
    path('pedidos/lista', views.ListaPedidoView.as_view(),
         name="lista_pedidos"),

    # GET/POST /pedidos/{pk}
    path('pedidos/<pk>', views.AtualizaPedidoView.as_view(),
         name="atualiza_pedido"),

    # GET/POST /clientes/excluir/{pk}
    path('pedidos/excluir/<pk>',
         views.DeletaPedidoView.as_view(), name="deleta_pedido"),

    path('delete-item/<int:pk>/', delete_item, name='delete_item'),

    #path('add-row/', views.add_row_pedido_items_hx, name='add_row_pedido_items_hx'),


]
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
