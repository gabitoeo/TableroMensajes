from django.shortcuts import render, redirect, get_object_or_404
from .models import Mensaje
from .forms import MensajeForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class CrearMensajeView(CreateView):
    model = Mensaje
    template_name = 'mensajes/crear_mensaje.html'
    fields = ['destinatario', 'contenido']
    success_url = reverse_lazy('ver_mensajes_enviados')

    def form_valid(self, form):
        usuario_predeterminado = User.objects.get(username='predeterminado')
        form.instance.remitente = usuario_predeterminado
        return super().form_valid(form)


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

