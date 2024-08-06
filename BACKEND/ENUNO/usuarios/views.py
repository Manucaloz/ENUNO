from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from asgiref.sync import sync_to_async
from .models import Usuarios
from .serializers import UsuariosSerializer
import json

@csrf_exempt
@require_http_methods(["GET", "POST"])
async def list_usuarios(request):
    """
    Vista para listar y crear usuarios.

    GET: Retorna una lista de todos los usuarios.
    POST: Crea un nuevo usuario con los datos proporcionados en la solicitud.

    Respuestas:
        - 200 OK: Solicitud GET exitosa.
        - 201 Created: Usuario creado exitosamente.
        - 400 Bad Request: Error de decodificación o JSON inválido.
    """
    if request.method == "GET":
        queryset = await sync_to_async(list)(Usuarios.objects.all())
        serializer = UsuariosSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        try:
            body = request.body
            data = body.decode('utf-8')
            json_data = json.loads(data)
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            return JsonResponse({'error': 'Error de decodificación o JSON: ' + str(e)}, status=400)
        
        serializer = UsuariosSerializer(data=json_data)
        is_valid = await sync_to_async(serializer.is_valid)()
        
        if is_valid:
            usuario = await sync_to_async(serializer.save)()
            return JsonResponse(UsuariosSerializer(usuario).data, status=201)
        
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@require_http_methods(["GET", "PUT", "PATCH", "DELETE"])
async def retrieve_usuario(request, pk):
    """
    Vista para recuperar, actualizar o eliminar un usuario específico.

    GET: Retorna los datos de un usuario específico.
    PUT/PATCH: Actualiza los datos de un usuario.
    DELETE: Elimina un usuario.

    Respuestas:
        - 200 OK: Solicitud GET, PUT o PATCH exitosa.
        - 204 No Content: Usuario eliminado exitosamente.
        - 400 Bad Request: Error de decodificación o JSON inválido.
        - 404 Not Found: Usuario no encontrado.
    """
    try:
        instance = await sync_to_async(Usuarios.objects.get)(pk=pk)
    except Usuarios.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    
    if request.method == 'GET':
        serializer = UsuariosSerializer(instance)
        return JsonResponse(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        try:
            body = request.body
            data = body.decode('utf-8')
            json_data = json.loads(data)
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            return JsonResponse({'error': 'Error de decodificación o JSON: ' + str(e)}, status=400)
        
        partial = request.method == "PATCH"
        serializer = UsuariosSerializer(instance, data=json_data, partial=partial)
        is_valid = await sync_to_async(serializer.is_valid)()
        
        if is_valid:
            await sync_to_async(serializer.save)()
            return JsonResponse(serializer.data)
        
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        await sync_to_async(instance.delete)()
        return HttpResponse(status=204)
