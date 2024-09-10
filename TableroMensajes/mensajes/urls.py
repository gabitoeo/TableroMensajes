from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_mensaje, name='crear_mensaje'),
    path('recibidos/', views.ver_mensajes_recibidos, name='ver_mensajes_recibidos'),
    path('enviados/', views.ver_mensajes_enviados, name='ver_mensajes_enviados'),
    path('eliminar/<int:pk>/', views.eliminar_mensaje, name='eliminar_mensaje'),
]
