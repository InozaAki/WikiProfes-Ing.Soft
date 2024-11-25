from django.urls import path
from . import views

app_name = 'usuario'
urlpatterns = [
    path('registro', views.RegistroForm.as_view(), name='registro'),
]