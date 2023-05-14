from django.db import models

# Create your models here.
from django.db import models


# classe cliente
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

    class Meta:
        db_table = "cliente"

    def __str__(self):
        return f"{self.nome}"

# classe status pedido


class StatusPedido(models.Model):

    descricao = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )

    objetos = models.Manager()

    class Meta:
        db_table = "status_pedido"

    def __str__(self):
        return f"{self.descricao}"

# classe pedido


class Pedido(models.Model):

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        db_column="id_cliente"

    )

    statusPedido = models.ForeignKey(
        StatusPedido,
        null=False,
        on_delete=models.NOT_PROVIDED,
        blank=False,
        db_column="id_status_pedido"
    )

    data_pedido = models.DateField(
        null=False,
        blank=False
    )
    valor_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    observacao = models.TextField(
        max_length=2000,
        null=True,
        blank=True
    )

    objetos = models.Manager()

    class Meta:
        db_table = "pedido"

# classe item_pedido


class ItemPedido(models.Model):

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        db_column="id_pedido"
    )

    descricao_item = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False
    )
    item_cancelado = models.BooleanField(
        null=False,
        default=False
    )
    observacao = models.CharField(
        max_length=2000,
        null=False,
        blank=False
    )

    objetos = models.Manager()

    class Meta:
        db_table = "item_pedido"
