from rest_framework import serializers
from .models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Usuarios.

    Convierte instancias del modelo Usuarios a JSON y viceversa. Incluye validación 
    adicional para la contraseña, la cual se maneja de forma privada.

    Meta:
        model (Model): El modelo asociado es Usuarios.
        fields (list): Lista de campos que se incluyen en la representación JSON.
        extra_kwargs (dict): Configuración adicional para campos específicos.
            - contrasena: Se especifica como write-only y requerida.
    """
    class Meta:
        model = Usuarios
        fields = ['id_usuario', 'id_restaurante', 'id_cargo', 'nombre', 'apellido', 'dni', 'usuario', 'contrasena']
        extra_kwargs = {
            'contrasena': {'write_only': True, 'required': True}
        }
