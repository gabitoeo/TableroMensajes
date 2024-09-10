from django.urls import path
from . import views
from .views import CrearMensajeView

urlpatterns = [
    path('crear/', CrearMensajeView.as_view(), name='crear_mensaje'),
    path('recibidos/', views.ver_mensajes_recibidos, name='ver_mensajes_recibidos'),
    path('enviados/', views.ver_mensajes_enviados, name='ver_mensajes_enviados'),
    path('eliminar/', views.eliminar_mensajes, name='eliminar_mensajes'),
]
