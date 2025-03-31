"""
Servicio: Serializador de usuarios.

Este archivo define el serializador para el modelo de usuarios. 
El serializador convierte instancias del modelo `User` en representaciones JSON 
y valida los datos enviados por el cliente.

Detalles:
- Campos serializados: `id`, `username`, `email`, `password`.

No requiere interacción directa del usuario.
"""

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

