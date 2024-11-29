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
        return Publicacion.objects.filter(profesor_id=self.kwargs['profesor_id']).order_by('-fecha')

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
    context_object_name = 'publicacion_list'

    def get_queryset(self):
        publicaciones = Publicacion.objects.filter(materia_id=self.kwargs['materia_id'])

        return publicaciones

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publicaciones = self.get_queryset()

        profesores_unicos = (
            publicaciones.values('profesor_id', 'profesor__nombre')
            .distinct()
        )
        context['profesores_unicos'] = profesores_unicos
        context['materia'] = Materia.objects.get(id=self.kwargs['materia_id'])
        return context

class DetallePublicacionView(generic.DetailView):
    model = Publicacion
    template_name = 'profesor/detalle_publicacion.html'
    context_object_name = 'publicacion'