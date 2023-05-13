from siscostura.models import Cliente
from django import forms


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