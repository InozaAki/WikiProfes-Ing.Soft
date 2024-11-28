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
        kwargs = super().get_form_kwargs()
        kwargs['usuario'] = self.request.user.id        
        return kwargs

    def form_valid(self, form):
        publicacion = form.storePublicacion()
        return redirect(self.success_url)
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        
        profesor = Profesor.objects.all()
        materia = Materia.objects.all()

        context['materias'] = materia
        context['profesores'] = profesor

        return context

class InicioSesionView(views.LoginView):
    template_name = 'usuario/inicio_sesion.html'
    redirect_authenticated_user = True
    next_page = 'usuario:index'

def logOutRequest(request):
    logout(request)
    return redirect(reverse_lazy('usuario:index'))

def busqueda(request):
    template_name = 'pages/busqueda.html'

    if request.method == 'POST':
        print("culos")



    return render(request, template_name)

class HomeView(generic.ListView):
    model = Publicacion
    template_name = 'pages/index.html'
    context_object_name = 'publicacion_list'

    def get_queryset(self):
        return Publicacion.objects.order_by('-fecha')[:5]