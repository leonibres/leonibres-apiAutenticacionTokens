from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


def home(request):
    """
    Servicio: Página de inicio.

    Este servicio devuelve un mensaje de bienvenida al acceder a la URL raíz.

    Método: GET
    URL: /
    Respuesta:
    - Mensaje de bienvenida (texto plano).
    """
    return HttpResponse("Bienvenido a la página de inicio.")


@api_view(['POST'])
def login(request):
    """
    Servicio: Inicio de sesión.

    Este servicio permite a los usuarios autenticarse proporcionando su nombre de usuario y contraseña.
    Devuelve un token de autenticación y los datos del usuario.

    Método: POST
    URL: /login
    Parámetros:
    - username: Nombre de usuario (string).
    - password: Contraseña del usuario (string).

    Respuesta:
    - token: Token de autenticación (string).
    - user: Datos del usuario autenticado (JSON).
    """
    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)  # Cambiar 'isinstance' por 'instance'

    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    """
    Servicio: Registro de usuario.

    Este servicio permite registrar un nuevo usuario proporcionando un nombre de usuario, contraseña y correo electrónico.
    Devuelve un token de autenticación y los datos del usuario registrado.

    Método: POST
    URL: /register
    Parámetros:
    - username: Nombre de usuario (string).
    - password: Contraseña del usuario (string).
    - email: Correo electrónico del usuario (string).

    Respuesta:
    - token: Token de autenticación (string).
    - user: Datos del usuario registrado (JSON).
    """
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        
        user = User.objects.get(username=request.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])  # Permitir métodos GET y POST
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    """
    Servicio: Perfil del usuario autenticado.

    Este servicio permite obtener los datos del usuario autenticado utilizando un token de autenticación.

    Método: GET, POST
    URL: /profile
    Requiere:
    - Autenticación mediante token.

    Respuesta:
    - Datos del usuario autenticado (JSON).
    """
    print(request.user.id)
    serializer = UserSerializer(instance=request.user)

    return Response(serializer.data, status=status.HTTP_200_OK)