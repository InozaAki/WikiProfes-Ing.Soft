from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegistroForm
from django.contrib.auth import views
from django.contrib.auth import logout
from publicacion.models import Publicacion

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
        #Usuario utilizado en login en el futuro
        return super().form_valid(form)

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