from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegistroForm, PublicacionForm
from django.contrib.auth import views
from django.contrib.auth import logout
from publicacion.models import Publicacion
from profesor.models import Profesor
from materia.models import Materia
from django import forms

# Create your views here.
class RegistroView(generic.FormView):
    template_name = 'usuario/registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('usuario:index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        usuario = form.storeUser()
        return super().form_valid(form)

class CrearPublicacion(generic.FormView):
    template_name = 'usuario/crear_publicacion.html'
    form_class = PublicacionForm
    success_url = reverse_lazy('usuario:index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        """Añadir el usuario actual a los argumentos del formulario."""
        kwargs = super().get_form_kwargs()
        kwargs['usuario'] = self.request.user
        return kwargs

    def form_valid(self, form):
        """Guardar la publicación si el formulario es válido."""
        publicacion = form.save(commit=False)
        publicacion.usuario = self.request.user
        publicacion.save()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        """Agregar el contexto de materias y profesores al formulario."""
        context = super().get_context_data(**kwargs)
        context['materias'] = Materia.objects.all()
        context['profesores'] = Profesor.objects.all()
        return context

class InicioSesionView(views.LoginView):
    template_name = 'usuario/inicio_sesion.html'
    redirect_authenticated_user = True
    next_page = 'usuario:index'

def logOutRequest(request):
    logout(request)
    return redirect(reverse_lazy('usuario:index'))

class HomeView(generic.ListView):
    model = Publicacion
    template_name = 'pages/index.html'
    context_object_name = 'publicacion_list'

    def get_queryset(self):
        return Publicacion.objects.order_by('-fecha')[:5]

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'comentario', 'materia', 'profesor', 'dominio', 'puntualidad', 'asistencia', 'dificultad', 'seguimiento']

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)