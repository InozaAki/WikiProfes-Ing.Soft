from django.shortcuts import render
from django.views import generic
from .models import Publicacion
from profesor.models import Profesor
from materia.models import Materia

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
    
class MateriaView(generic.ListView):
    template_name = 'materia/materiaDetalles.html'

    def get_queryset(self):
        materia = Publicacion.objects.filter(materia_id=self.kwargs['materia_id'])

        if not materia:
            materia = Materia.objects.filter(id=self.kwargs['materia_id'])

        return materia

class DetallePublicacionView(generic.DetailView):
    model = Publicacion
    template_name = 'profesor/detalle_publicacion.html'
    context_object_name = 'publicacion'