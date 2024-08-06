from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from asgiref.sync import sync_to_async
import json
from .models import Alimentos
from .serializers import AlimentosSerializer

@csrf_exempt
@require_http_methods(["GET", "POST"])
async def alimentos_list(request):
    """
    Maneja las solicitudes GET y POST para la lista de alimentos.

    - **GET**: Obtiene una lista de todos los alimentos en la base de datos. 
      Utiliza `sync_to_async` para realizar la consulta de manera asíncrona y 
      devuelve los datos en formato JSON.
    - **POST**: Crea un nuevo alimento con los datos proporcionados en el cuerpo 
      de la solicitud. Valida los datos y, si son válidos, guarda el nuevo objeto 
      en la base de datos y devuelve los datos del alimento creado en formato JSON.

    Args:
        request (HttpRequest): La solicitud HTTP que se maneja.

    Returns:
        JsonResponse: Respuesta JSON con los datos de los alimentos o errores de 
        validación. Para una solicitud POST exitosa, se devuelve un estado 201; 
        para errores de validación, se devuelve un estado 400.
    """
    if request.method == 'GET':
        # Utiliza sync_to_async para la consulta a la base de datos
        queryset = await sync_to_async(list)(Alimentos.objects.all())
        serializer = AlimentosSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = AlimentosSerializer(data=data)
        if serializer.is_valid():
            # Utiliza sync_to_async para guardar el nuevo objeto
            await sync_to_async(serializer.save)()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
async def alimentos_detail(request, pk):
    """
    Maneja las solicitudes GET, PUT y DELETE para un alimento específico.

    - **GET**: Obtiene los detalles de un alimento específico por su ID (`pk`). 
      Utiliza `sync_to_async` para obtener el objeto de manera asíncrona y devuelve 
      los datos en formato JSON. Si el alimento no existe, devuelve un estado 404.
    - **PUT**: Actualiza un alimento específico con los datos proporcionados en 
      el cuerpo de la solicitud. Valida los datos y, si son válidos, guarda los 
      cambios en la base de datos. Devuelve los datos actualizados en formato JSON 
      o errores de validación. Si el alimento no existe, devuelve un estado 404.
    - **DELETE**: Elimina un alimento específico por su ID (`pk`) de la base de datos. 
      Utiliza `sync_to_async` para eliminar el objeto de manera asíncrona. Devuelve 
      un estado 204 si la eliminación es exitosa, o un estado 404 si el alimento no existe.

    Args:
        request (HttpRequest): La solicitud HTTP que se maneja.
        pk (int): El identificador único del alimento a manejar.

    Returns:
        JsonResponse: Respuesta JSON con los datos del alimento o errores de validación 
        para una solicitud PUT. 
        HttpResponse: Respuesta HTTP con un estado 204 para una eliminación exitosa 
        o un estado 404 si el alimento no existe.
    """
    if request.method == 'GET':
        try:
            # Utiliza sync_to_async para obtener el objeto de la base de datos
            instance = await sync_to_async(Alimentos.objects.get)(pk=pk)
            serializer = AlimentosSerializer(instance)
            return JsonResponse(serializer.data)
        except Alimentos.DoesNotExist:
            return HttpResponse(status=404)

    elif request.method == 'PUT':
        try:
            # Utiliza sync_to_async para obtener el objeto de la base de datos
            instance = await sync_to_async(Alimentos.objects.get)(pk=pk)
            data = json.loads(request.body)
            serializer = AlimentosSerializer(instance, data=data, partial=True)
            if serializer.is_valid():
                # Utiliza sync_to_async para guardar los cambios
                await sync_to_async(serializer.save)()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
        except Alimentos.DoesNotExist:
            return HttpResponse(status=404)

    elif request.method == 'DELETE':
        try:
            # Utiliza sync_to_async para obtener el objeto de la base de datos
            instance = await sync_to_async(Alimentos.objects.get)(pk=pk)
            # Utiliza sync_to_async para eliminar el objeto
            await sync_to_async(instance.delete)()
            return HttpResponse(status=204)
        except Alimentos.DoesNotExist:
            return HttpResponse(status=404)
