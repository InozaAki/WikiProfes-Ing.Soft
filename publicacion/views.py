from django.shortcuts import render
from django.views import generic
from .models import Publicacion
from profesor.models import Profesor

# Create your views here.
class ProfesorView(generic.ListView):
    template_name = 'profesor/profesorPerfil.html'
    context_object_name = 'publicaciones'

    def get_queryset(self):
        return Publicacion.objects.filter(profesor_id=self.kwargs['profesor_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        profesor = Profesor.objects.get(id=self.kwargs['profesor_id'])
        rangoEstrellas = range(1, 6)
        context['profesor'] = profesor
        context['promedios'] = profesor.promedioCriterios
        context['promedioGeneral'] = profesor.promedioGeneral
        context['rangoEstrellas'] = rangoEstrellas
        return context