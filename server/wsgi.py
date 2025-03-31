"""
Servicio: Configuración WSGI.

Este archivo configura la interfaz WSGI para el proyecto Django. 
Es utilizado para desplegar la aplicación en servidores compatibles con WSGI.

Detalles:
- Expone la variable `application` como el punto de entrada WSGI.
- Configura el entorno de Django para el despliegue.

No requiere interacción directa del usuario.
"""

"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()
