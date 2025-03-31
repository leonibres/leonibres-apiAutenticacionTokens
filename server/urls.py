"""
Servicio: Configuración de URLs.

Este archivo define las rutas disponibles en el proyecto Django. 
Cada ruta está asociada a una vista que maneja las solicitudes correspondientes.

Detalles:
- `/admin/`: Acceso al panel de administración de Django.
- `/login`: Endpoint para iniciar sesión.
- `/register`: Endpoint para registrar un nuevo usuario.
- `/profile`: Endpoint para consultar el perfil del usuario autenticado.
- `/`: Página de inicio.

No requiere interacción directa del usuario para configurarse.
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views  # Replace 'my_app' with the actual app name where views.py is located

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('login', views.login),
    re_path('register', views.register),
    re_path('profile', views.profile),
    path('', views.home, name='home'),  # Ruta para la URL raíz
]
