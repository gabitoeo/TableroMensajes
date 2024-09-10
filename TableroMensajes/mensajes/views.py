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
    usuario_predeterminado = User.objects.get(username='predeterminado')
    mensajes = Mensaje.objects.filter(destinatario=usuario_predeterminado)
    return render(request, 'mensajes/mensajes_recibidos.html', {'mensajes': mensajes})

def ver_mensajes_enviados(request):
    usuario_predeterminado = User.objects.get(username='predeterminado')
    mensajes = Mensaje.objects.filter(remitente=usuario_predeterminado)
    return render(request, 'mensajes/mensajes_enviados.html', {'mensajes': mensajes})

def eliminar_mensajes(request):
    usuario_predeterminado = User.objects.get(username='predeterminado')

    if request.method == 'POST':
        mensajes_ids = request.POST.getlist('mensajes_ids')
        mensajes = Mensaje.objects.filter(pk__in=mensajes_ids, remitente=usuario_predeterminado)
        
        mensajes.delete()
        return redirect('ver_mensajes_enviados')  

    mensajes = Mensaje.objects.filter(remitente=usuario_predeterminado)
    return render(request, 'mensajes/eliminar_mensajes.html', {'mensajes': mensajes})

