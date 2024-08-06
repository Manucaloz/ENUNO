from django.db import models

class Pedidos(models.Model):
    """
    Modelo que representa un pedido en el sistema.

    Atributos:
        - id_pedidos (AutoField): Identificador único del pedido.
        - id_usuario (IntegerField): Identificador del usuario que realizó el pedido.
        - id_mesa (IntegerField): Identificador de la mesa donde se realizó el pedido.
        - fecha_hora (DateTimeField): Fecha y hora en que se realizó el pedido. Puede ser nulo.
        - estado_pedido (CharField): Estado actual del pedido. Puede ser nulo y se limita a 10 caracteres.

    Meta:
        managed (bool): Indica si el modelo es gestionado por Django (False en este caso).
        db_table (str): Nombre de la tabla en la base de datos ('pedidos').
    """
    id_pedidos = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    id_mesa = models.IntegerField()
    fecha_hora = models.DateTimeField(db_column='Fecha_hora', blank=True, null=True)  # Nombre de campo en minúsculas.
    estado_pedido = models.CharField(db_column='Estado_pedido', max_length=10, blank=True, null=True)  # Nombre de campo en minúsculas.

    class Meta:
        managed = False
        db_table = 'pedidos'
