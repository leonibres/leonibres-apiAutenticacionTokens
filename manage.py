#!/usr/bin/env python
"""
Servicio: Herramienta de administración de Django.

Este archivo permite ejecutar tareas administrativas para el proyecto Django, 
como iniciar el servidor de desarrollo, realizar migraciones, crear superusuarios, entre otros.

Detalles:
- Configura el entorno de Django.
- Ejecuta comandos administrativos a través de la línea de comandos.

Ejemplo de uso:
- `python manage.py runserver` para iniciar el servidor de desarrollo.
- `python manage.py migrate` para aplicar migraciones de base de datos.
"""
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
