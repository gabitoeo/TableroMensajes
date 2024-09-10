from django.shortcuts import render, redirect, get_object_or_404
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.models import User

def crear_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            
            mensaje.remitente = User.objects.get(username='predeterminado') 
            mensaje.save()
            return redirect('ver_mensajes_enviados')
    else:
        form = MensajeForm()
    
    return render(request, 'mensajes/crear_mensaje.html', {'form': form})


def ver_mensajes_recibidos(request):
    # Usar el usuario predeterminado para esta vista
    usuario_predeterminado = User.objects.get(username='predeterminado')
    mensajes = Mensaje.objects.filter(destinatario=usuario_predeterminado)
    return render(request, 'mensajes/mensajes_recibidos.html', {'mensajes': mensajes})

def ver_mensajes_enviados(request):
    # Siempre usar el usuario predeterminado para esta vista
    usuario_predeterminado = User.objects.get(username='predeterminado')
    mensajes = Mensaje.objects.filter(remitente=usuario_predeterminado)
    return render(request, 'mensajes/mensajes_enviados.html', {'mensajes': mensajes})

def eliminar_mensajes(request):
    # Obtener el usuario predeterminado
    usuario_predeterminado = User.objects.get(username='predeterminado')

    if request.method == 'POST':
        # Obtener los IDs de los mensajes seleccionados
        mensajes_ids = request.POST.getlist('mensajes_ids')
        mensajes = Mensaje.objects.filter(pk__in=mensajes_ids, remitente=usuario_predeterminado)
        
        # Eliminar los mensajes seleccionados
        mensajes.delete()
        return redirect('ver_mensajes_enviados')  # Redirigir después de la eliminación

    # Mostrar la página con los mensajes
    mensajes = Mensaje.objects.filter(remitente=usuario_predeterminado)
    return render(request, 'mensajes/eliminar_mensajes.html', {'mensajes': mensajes})

