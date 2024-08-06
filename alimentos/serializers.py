from rest_framework import serializers
from .models import Alimentos

class AlimentosSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Alimentos.

    Este serializador convierte instancias del modelo `Alimentos` 
    en representaciones JSON y viceversa. Utiliza `ModelSerializer` 
    para proporcionar una implementación rápida y simple para la 
    serialización y deserialización de los datos del modelo.

    Atributos:
        Meta (class): Configuración del serializador que especifica el 
                      modelo asociado y los campos que deben incluirse 
                      en la serialización/deserialización. En este caso, 
                      se incluyen todos los campos del modelo `Alimentos`.
    """
    
    class Meta:
        model = Alimentos
        fields = '__all__'
from rest_framework import serializers
from .models import Alimentos
from .validators import validate_nombre, validate_precio

class AlimentosSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Alimentos.

    Este serializador convierte instancias del modelo `Alimentos` en representaciones JSON 
    y viceversa. Utiliza `ModelSerializer` para proporcionar una implementación rápida 
    y sencilla para la serialización y deserialización de los datos del modelo.

    Campos personalizados:
        nombre (CharField): Campo de texto con validación para asegurar que solo contenga 
        caracteres alfanuméricos y espacios.
        precio (DecimalField): Campo decimal con validación para asegurar que el precio no 
        sea negativo. Puede ser nulo y no es obligatorio.

    Atributos:
        Meta (class): Configuración del serializador que especifica el modelo asociado 
                      y los campos que deben incluirse en la serialización/deserialización.
    """
    
    nombre = serializers.CharField(validators=[validate_nombre], required=False, allow_null=True)
    precio = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[validate_precio],
        required=False,
        allow_null=True
    )

    class Meta:
        model = Alimentos
        fields = '__all__'
