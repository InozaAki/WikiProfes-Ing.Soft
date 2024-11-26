from django.urls import path
from . import views

app_name = 'materia'
urlpatterns = [
    path('materias', views.MateriasView.as_view(), name='materias'),
]