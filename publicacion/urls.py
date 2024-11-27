from django.urls import path
from . import views

app_name = 'publicacion'
urlpatterns = [
    path('profesor/<int:profesor_id>', views.ProfesorView.as_view(), name='profesor'),
    path('materia/<int:materia_id>', views.MateriaView.as_view(), name='materia'),
    path('<int:pk>/', views.DetallePublicacionView.as_view(), name='detalle'),
]