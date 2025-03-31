"""
Servicio: Configuración ASGI.

Este archivo configura la interfaz ASGI para el proyecto Django.
Es utilizado para desplegar la aplicación en servidores compatibles con ASGI, 
permitiendo soporte para aplicaciones asincrónicas.

Detalles:
- Expone la variable `application` como el punto de entrada ASGI.
- Configura el entorno de Django para el despliegue.

No requiere interacción directa del usuario.
"""

"""
ASGI config for server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_asgi_application()
