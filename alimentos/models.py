from django.db import models

class Alimentos(models.Model):
    """
    Modelo que representa un alimento en la base de datos.

    Atributos:
        id_alimentos (int): Identificador único para cada alimento. Utiliza un campo AutoField para autoincrementarse automáticamente.
        nombre (str): Nombre del alimento. Campo de texto con un máximo de 45 caracteres. Puede ser blanco o nulo.
        precio (Decimal): Precio del alimento. Campo decimal con hasta 10 dígitos en total y 2 decimales. Puede ser blanco o nulo.

    La clase Meta contiene configuraciones adicionales:
        managed (bool): Indica que Django no debe gestionar la creación ni la eliminación de la tabla en la base de datos. Asume que la tabla ya existe.
        db_table (str): Nombre de la tabla en la base de datos que corresponde a este modelo.
    """
    
    id_alimentos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alimentos'
