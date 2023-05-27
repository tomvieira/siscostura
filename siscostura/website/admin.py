from django.contrib import admin
from siscostura.models import Pedido
from siscostura.models import StatusPedido
from siscostura.models import Cliente
from siscostura.models import ItemPedido

# Register your models here.

admin.site.register(Pedido)
admin.site.register(StatusPedido)
admin.site.register(Cliente)
admin.site.register(ItemPedido)
admin.site.site_header = "Administração SisCostura"