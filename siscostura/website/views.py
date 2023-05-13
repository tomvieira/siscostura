from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from siscostura.models import Cliente
from django.urls import reverse_lazy
from .forms import InsereClienteForm

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
