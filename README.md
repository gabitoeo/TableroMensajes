# TableroMensajes
Trabajo Practico N2 - Programacion Web II
Proyecto Django para la gestión de mensajes.

## Descripción
Este proyecto permite a un usuario predeterminado crear, ver y eliminar mensajes sin necesidad de autenticarse. Está desarrollado usando el framework Django y sigue el patrón Modelo-Vista-Plantilla (MVT).

## Instalación
Serie de pasos para instalar y ejecutar el proyecto localmente:

1. Clona el repositorio:
  git clone https://github.com/gabitoeo/TableroMensajes.git
2. Navega al directorio del proyecto
  cd TableroMensajes
3. Crea un Entorno virtual
  virtualenv 'nombre_del_entorno'
4. Activar el entorno
  source 'nombre_del_entorno'/bin/activate
5. Instalar las dependencias de requirements.txt
  pip install -r requirements.txt
6. Realizar las migraciones
  python manage.py migrate
7. Ejecutar el servidor
  python manage.py runserver

## Funcionalidades
1. Crear un mensaje /mensajes/crear
2. Ver mensajes enviados /mensajes/enviados
3. Ver mensajes recibidos /mensajes/recibidos
4. ELiminar un mensajes /mensajes/eliminar

## Dependencias 
Django
Python



  
