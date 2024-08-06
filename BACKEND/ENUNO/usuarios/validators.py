from rest_framework import serializers
from .models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Usuarios.

    Este serializador convierte todas las instancias del modelo Usuarios a 
    representaciones JSON y viceversa.

    Meta:
        model (Model): El modelo asociado es Usuarios.
        fields (str): Indica que todos los campos del modelo se incluyen en 
                      la representación JSON.
    """
    class Meta:
        model = Usuarios
        fields = '__all__'
