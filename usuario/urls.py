from django.urls import path
from . import views

app_name = 'usuario'
urlpatterns = [
    path('registro', views.RegistroView.as_view(), name='registro'),
    path('inicio-sesion', views.InicioSesionView.as_view(), name='inicio-sesion'),
    path('', views.HomeView.as_view(), name='index'),
    path('logout', views.logOutRequest, name='logout'),
    path('crear-publicacion', views.CrearPublicacion.as_view(), name='crear-publicacion'),
]