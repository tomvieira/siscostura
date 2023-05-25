from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from siscostura.models import Cliente
from siscostura.models import Pedido
from .forms import InserePedidoForm
from django.urls import reverse_lazy
from .forms import InsereClienteForm
from django.urls import reverse_lazy
from .forms import ItemPedidoFormSet
from .forms import ItemPedidoForm
from siscostura.models import ItemPedido
from django.contrib import messages

# Create your views here.


# PÁGINA PRINCIPAL
# ----------------------------------------------

class HomeView(TemplateView):
    template_name = "website/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()

        return context


# PÁGINA PRINCIPAL CLIENTES
# ----------------------------------------------

class HomeClienteView(TemplateView):
    template_name = "website/clientes/index.html"


# LISTA DE CLIENTES
# ----------------------------------------------

class ListaclientesView(ListView):
    template_name = "website/clientes/lista.html"
    model = Cliente
    context_object_name = "clientes"


# CADASTRAMENTO DE CLIENTES
# ----------------------------------------------

class CriaClienteView(CreateView):
    template_name = "website/clientes/cria.html"
    model = Cliente
    form_class = InsereClienteForm
    success_url = reverse_lazy("website:lista_clientes")


# ATUALIZAÇÃO DE CLIENTES
# ----------------------------------------------

class AtualizaClienteView(UpdateView):
    template_name = "website/clientes/atualiza.html"
    model = Cliente
    fields = '__all__'
    context_object_name = 'Cliente'
    success_url = reverse_lazy("website:lista_clientes")


# EXCLUSÃO DE CLIENTES
# ----------------------------------------------

class DeletaClienteView(DeleteView):
    template_name = "website/clientes/exclui.html"
    model = Cliente
    context_object_name = 'Cliente'
    success_url = reverse_lazy("website:lista_clientes")


# PÁGINA PRINCIPAL PEDIDOS
# ----------------------------------------------

class HomePedidoView(TemplateView):
    template_name = "website/pedidos/index.html"

# LISTA DE PEDIDOS
# ----------------------------------------------


class ListaPedidoView(ListView):
    template_name = "website/pedidos/lista.html"
    model = Pedido
    context_object_name = "pedidos"


# CADASTRAMENTO DE PEDIDOS
# ----------------------------------------------
class PedidoInline():
    form_class = InserePedidoForm
    model = Pedido
    template_name = "website/pedidos/cria.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()
        

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_items_pedido_valid', None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('/pedidos/lista')

    def formset_items_pedido_valid(self, formset):
        """
        Hook for custom formset saving.. useful if you have multiple formsets
        """
        items_pedido = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this, if you have can_delete=True parameter set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for item_pedido in items_pedido:
            item_pedido.pedido = self.object
            item_pedido.save()


class CriaPedidoView(PedidoInline,CreateView):
     
    def get_context_data(self, **kwargs):
        ctx = super(CriaPedidoView, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'item_pedido': ItemPedidoFormSet(prefix='items'),                
            }
        else:
            return {
                'item_pedido': ItemPedidoFormSet(self.request.POST or None, self.request.FILES or None, prefix='items'),                
            }




# ATUALIZAÇÃO DE PEDIDOS
# ----------------------------------------------

class AtualizaPedidoView(PedidoInline,UpdateView):
   def get_context_data(self, **kwargs):
        ctx = super(AtualizaPedidoView, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx
   
   def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'items': ItemPedidoFormSet(prefix='items'),   
            }
        else:
            return {
                'items': ItemPedidoFormSet(self.request.POST or None, self.request.FILES or None, prefix='items'),                
            }


# EXCLUSÃO DE PEDIDOS
# ----------------------------------------------

class DeletaPedidoView(DeleteView):
    template_name = "website/pedidos/exclui.html"
    model = Pedido
    context_object_name = 'Pedido'
    success_url = reverse_lazy("website:lista_pedidos")

def delete_item(request, pk):
    try:
        itemPedido = ItemPedido.objetos.get(id=pk)
    except ItemPedido.DoesNotExist:
        messages.success(
            request, 'Objeto não encontrado'
            )
        return redirect('website:atualiza_pedido', pk=itemPedido.pedido.id)


