from django.db import models

class Caja(models.Model):
    """
    Modelo que representa un registro en la caja de ventas.

    Este modelo se utiliza para almacenar información sobre las transacciones realizadas en la caja, incluyendo 
    detalles de pedidos y órdenes, así como el total y la fecha de la transacción.

    Atributos:
        id_caja (AutoField): La clave primaria para el registro en la caja. Se incrementa automáticamente.
        id_pedido (IntegerField): El identificador del pedido asociado con esta transacción. Este campo es opcional.
        id_ordenes (IntegerField): El identificador de las órdenes asociadas con esta transacción. Este campo es opcional.
        total (IntegerField): El total de la transacción en la caja. Este campo es opcional.
        fecha (DateField): La fecha en que se realizó la transacción. Este campo es opcional.

    Meta:
        managed (bool): Especifica si Django debe gestionar el esquema de la base de datos para este modelo. 
                        En este caso, es False, lo que significa que Django no creará, modificará ni eliminará 
                        la tabla en la base de datos para este modelo.
        db_table (str): El nombre de la tabla en la base de datos asociada con este modelo. En este caso, la 
                        tabla se llama 'caja'.
    """
    id_caja = models.AutoField(primary_key=True)
    id_pedido = models.IntegerField(blank=True, null=True)
    id_ordenes = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caja'
