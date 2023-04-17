from django.db import models

# Create your models here.
from django.db import models


class Cliente(models.Model):
    nome = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )
    data_nascimento = models.DateField(
        null=True,
        blank=True
    )
    cpf = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )
    telefone = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )
    endereco_logradouro = models.CharField(
        max_length=300,
        null=True,
        blank=True
    )
    endereco_numero = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    endereco_complemento = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    endereco_complemento = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    endereco_cep = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )
    endereco_bairro = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    endereco_cidade = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    endereco_estado = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    observacao = models.TextField(
        max_length=2000,
        null=True,
        blank=True
    )


objetos = models.Manager()
