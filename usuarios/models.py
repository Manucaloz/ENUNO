from django.db import models

class Usuarios(models.Model):
    """
    Modelo que representa un usuario en el sistema.

    Atributos:
        - id_usuario (AutoField): Identificador único del usuario.
        - id_restaurante (IntegerField): Identificador del restaurante asociado.
        - id_cargo (IntegerField): Identificador del cargo del usuario.
        - nombre (CharField): Nombre del usuario, con un máximo de 45 caracteres.
        - apellido (CharField): Apellido del usuario, con un máximo de 45 caracteres.
        - dni (CharField): Documento Nacional de Identidad del usuario, único y con un máximo de 8 caracteres.
        - usuario (CharField): Nombre de usuario, único y con un máximo de 45 caracteres.
        - contrasena (CharField): Contraseña del usuario, con un máximo de 45 caracteres.

    Meta:
        - managed (bool): Indica si el modelo es gestionado por Django (False en este caso).
        - db_table (str): Nombre de la tabla en la base de datos ('usuarios').
    """
    id_usuario = models.AutoField(primary_key=True)
    id_restaurante = models.IntegerField()
    id_cargo = models.IntegerField()
    nombre = models.CharField(db_column='Nombre', max_length=45)
    apellido = models.CharField(db_column='Apellido', max_length=45)
    dni = models.CharField(db_column='DNI', unique=True, max_length=8)  # Administrado como cadena para preservar ceros a la izquierda
    usuario = models.CharField(db_column='Usuario', unique=True, max_length=45)
    contrasena = models.CharField(db_column='Contraseña', max_length=45)

    class Meta:
        managed = False
        db_table = 'usuarios'
