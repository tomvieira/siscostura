from siscostura.models import Cliente
from siscostura.models import Pedido
from siscostura.models import ItemPedido
from django import forms
from django.forms import inlineformset_factory

# FORMULÁRIO DE INCLUSÃO DE CLIENTES
# -------------------------------------------

class InsereClienteForm(forms.ModelForm):

    observacao = forms.CharField(
        label='Observação',
        required=False,
        widget=forms.Textarea
    )

    data_nascimento = forms.DateField(
        label='Data nascimento',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    ESTADOS = (('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'),
               ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'))
    endereco_estado = forms.ChoiceField(choices=ESTADOS)

    class Meta:
        # Modelo base
        model = Cliente

        # Campos que estarão no form
        fields = [
            'nome',
            'data_nascimento',
            'cpf',
            'telefone',
            'endereco_logradouro',
            'endereco_numero',
            'endereco_complemento',
            'endereco_cep',
            'endereco_bairro',
            'endereco_cidade',
            'endereco_estado',
            'observacao',
        ]

# FORMULÁRIO DE INCLUSÃO DE PEDIDOS
# -------------------------------------------


class InserePedidoForm(forms.ModelForm):

    observacao = forms.CharField(
        label='Observação',
        required=False,
        widget=forms.Textarea
    )

    cliente = forms.ModelChoiceField(
        label='Cliente',        
        queryset=Cliente.objetos.all().order_by('nome'),
        required=True,
        
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    data_pedido = forms.DateField(
        label='Data pedido',
        required=False,
        widget=forms.DateInput(format='%d/%m/%Y')
    )

    class Meta:
        # Modelo base
        model = Pedido

        fields = '__all__'

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = '__all__'

ItemPedidoFormSet = inlineformset_factory(
    Pedido, ItemPedido, form=ItemPedidoForm,
    extra=1, can_delete=True,
    can_delete_extra=True
)