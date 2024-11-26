from django.urls import path
from . import views

app_name = 'publicacion'
urlpatterns = [
    path('profesor/<int:profesor_id>', views.ProfesorView.as_view(), name='profesor'),
    path('materia/<int:materia_id>', views.MateriaView.as_view(), name='materia'),
]