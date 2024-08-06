from django.db import models

class Bebidas(models.Model):
    """
    Un modelo de Django que representa una bebida.

    Este modelo se usa para almacenar información sobre las bebidas en la base de datos.

    Atributos:
        id_bebidas (AutoField): La clave primaria para el registro de la bebida. Se incrementa automáticamente.
        nombre (CharField): El nombre de la bebida. Es una cadena con una longitud máxima de 45 caracteres. Este campo es opcional.
        precio (DecimalField): El precio de la bebida. Es un número decimal con hasta 10 dígitos en total y 2 dígitos después del punto decimal. Este campo es opcional.

    Meta:
        managed (bool): Especifica si Django debe gestionar el esquema de la base de datos para este modelo. Si es False, Django no creará, modificará ni eliminará la tabla de la base de datos para este modelo.
        db_table (str): El nombre de la tabla de la base de datos asociada con este modelo. En este caso, la tabla se llama 'bebidas'.
    """
    id_bebidas = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bebidas'
