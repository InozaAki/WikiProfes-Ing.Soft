from django.shortcuts import render
from django.views import generic
from itertools import groupby
from .models import Materia

# Create your views here.
class MateriasView(generic.ListView):
    template_name = 'pages/materias.html'
    
    context_object_name = 'departamentos'

    def get_queryset(self):
        return Materia.objects.order_by('departamento', 'nombre')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        materias = self.get_queryset()

        departamentos = {}

        for departamento, grupo in groupby(materias, lambda x: x.departamento):
            departamentos[departamento] = list(grupo)

        context['departamentos'] = departamentos

        return context
