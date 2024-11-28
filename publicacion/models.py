from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from materia.models import Materia
from profesor.models import Profesor
from django.contrib.auth.models import User

# Create your models here.
class Publicacion(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=80)
    fecha = models.DateField(auto_now_add=True)  # Fecha automática al crear
    comentario = models.TextField(max_length=2000)
    
    # Campos con validaciones de rango
    dominio = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        help_text="Valor entre 0 y 10"
    )
    puntualidad = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        help_text="Valor entre 0 y 10"
    )
    asistencia = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        help_text="Valor entre 0 y 10"
    )
    dificultad = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        help_text="Valor entre 0 y 10"
    )
    seguimiento = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        help_text="Valor entre 0 y 10"
    )

    def __str__(self):
        return f'-| {self.titulo} |- publicado por: {self.usuario}'
