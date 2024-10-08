# Generated by Django 5.0.7 on 2024-07-28 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id_pedidos', models.AutoField(primary_key=True, serialize=False)),
                ('id_usuario', models.IntegerField()),
                ('id_mesa', models.IntegerField()),
                ('fecha_hora', models.DateTimeField(blank=True, db_column='Fecha_hora', null=True)),
                ('estado_pedido', models.CharField(blank=True, db_column='Estado_pedido', max_length=10, null=True)),
            ],
            options={
                'db_table': 'pedidos',
                'managed': False,
            },
        ),
    ]
