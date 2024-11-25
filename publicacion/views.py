from django.shortcuts import render
from django.views import generic
from .models import Publicacion

# Create your views here.
class PublicacionView(generic.ListView):
    def get_queryset(self):
        return Publicacion.objects.order_by('-fecha')[:5]