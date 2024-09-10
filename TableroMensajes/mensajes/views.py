from django.shortcuts import render, redirect, get_object_or_404
from .models import Mensaje
from .forms import MensajeForm

def crear_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user  
            mensaje.save()
            return redirect('ver_mensajes_enviados')
    else:
        form = MensajeForm()
    return render(request, 'mensajes/crear_mensaje.html', {'form': form})


def ver_mensajes_recibidos(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user)
    return render(request, 'mensajes/mensajes_recibidos.html', {'mensajes': mensajes})


def ver_mensajes_enviados(request):
    mensajes = Mensaje.objects.filter(remitente=request.user)
    return render(request, 'mensajes/mensajes_enviados.html', {'mensajes': mensajes})


def eliminar_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk, remitente=request.user)
    if request.method == 'POST':
        mensaje.delete()
        return redirect('ver_mensajes_enviados')
    return render(request, 'mensajes/eliminar_mensaje.html', {'mensaje': mensaje})
