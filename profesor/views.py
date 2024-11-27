from django.shortcuts import render
from django.views import generic
from .models import Profesor

# Create your views here.
class ProfesoresView(generic.ListView):
    template_name = 'pages/profesores.html'

    def get_queryset(self):
        return Profesor.objects.order_by('-nombre')[:5]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rangoEstrellas = range(1, 6)
        context['rangoEstrellas'] = rangoEstrellas
        
        return context