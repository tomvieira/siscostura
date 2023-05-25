# Generated by Django 4.2 on 2023-05-25 00:36

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("siscostura", "0002_alter_cliente_managers_alter_cliente_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="StatusPedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descricao", models.CharField(max_length=300)),
            ],
            options={
                "db_table": "status_pedido",
            },
            managers=[
                ("objetos", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Pedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_pedido", models.DateField()),
                (
                    "valor_total",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "observacao",
                    models.TextField(blank=True, max_length=2000, null=True),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        db_column="id_cliente",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="siscostura.cliente",
                    ),
                ),
                (
                    "statusPedido",
                    models.ForeignKey(
                        db_column="id_status_pedido",
                        on_delete=django.db.models.fields.NOT_PROVIDED,
                        to="siscostura.statuspedido",
                    ),
                ),
            ],
            options={
                "db_table": "pedido",
            },
            managers=[
                ("objetos", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="ItemPedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descricao_item", models.CharField(max_length=300)),
                ("preco", models.DecimalField(decimal_places=2, max_digits=10)),
                ("item_cancelado", models.BooleanField(default=False)),
                ("observacao", models.CharField(max_length=2000)),
                (
                    "pedido",
                    models.ForeignKey(
                        db_column="id_pedido",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="siscostura.pedido",
                    ),
                ),
            ],
            options={
                "db_table": "item_pedido",
            },
            managers=[
                ("objetos", django.db.models.manager.Manager()),
            ],
        ),
    ]
