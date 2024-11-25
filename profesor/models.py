from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg    

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=80)
    usuarios = models.ManyToManyField(User, through='publicacion.Publicacion')

    @property
    def promedioCriterios(self):
        publicaciones = self.publicacion_set.all()

        if not publicaciones.exists():
            return {'dominio':0, 'puntualidad':0, 'asistencia':0, 'dificultad':0, 'seguimiento':0}

        criterios = ['dominio', 'puntualidad', 'asistencia', 'dificultad', 'seguimiento']

        promedios = {}

        for criterio in criterios:
            promedio = publicaciones.aggregate(promedio=Avg(criterio))['promedio'] or 0
            promedios[criterio] = round(promedio, 2)

        return promedios

    @property
    def promedioGeneral(self):
        publicaciones = self.publicacion_set.all()

        if not publicaciones.exists():
            return 0

        promedioTotal = publicaciones.aggregate(
            promedio = models.Avg(
                (models.F('dominio')+models.F('puntualidad')+
                models.F('asistencia')+models.F('dificultad')+
                models.F('seguimiento')) / 5
            )
        )['promedio']

        return round(promedioTotal / 2)
    
    def __str__(self):
        return f'{self.nombre}'