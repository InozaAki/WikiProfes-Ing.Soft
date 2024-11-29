from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from publicacion.models import Publicacion
from profesor.models import Profesor
from materia.models import Materia

class RegistroForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    password2 = forms.CharField()

    def clean_username(self):
        usuario = self.cleaned_data.get('username')
        if User.objects.filter(username=usuario):
            raise forms.ValidationError('El usuario ya existe')
        return usuario

    def clean_email(self):
        correo = self.cleaned_data.get('email')
        if '@alumnos.udg.mx' not in correo:
            raise forms.ValidationError('Correo no valido, utiliza correo institucional UDG')
        if User.objects.filter(email=correo):
            raise forms.ValidationError('Ya existe usuario registrado con ese correo')
        return correo
    
    def storeUser(self):
        self.cleaned_data.pop('password2')
        return User.objects.create_user(**self.cleaned_data)
    
    
    def clean(self):  
        datos = self.cleaned_data;

        password = datos.get('password')
        confirmationPassword = datos.get('password2')

        if password != confirmationPassword:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return datos


class PublicacionForm(forms.Form):
    materia = forms.IntegerField()
    profesor = forms.IntegerField()
    titulo = forms.CharField()
    comentario = forms.CharField(widget=forms.TextInput())
    dominio = forms.IntegerField()
    puntualidad = forms.IntegerField()
    asistencia = forms.IntegerField()
    dificultad = forms.IntegerField()
    seguimiento = forms.IntegerField()

    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario = usuario

    def clean_dominio(self):
        return self.validate_range(self.cleaned_data.get('dominio'), 'Dominio')

    def clean_puntualidad(self):
        return self.validate_range(self.cleaned_data.get('puntualidad'), 'Puntualidad')

    def clean_asistencia(self):
        return self.validate_range(self.cleaned_data.get('asistencia'), 'Asistencia')

    def clean_dificultad(self):
        return self.validate_range(self.cleaned_data.get('dificultad'), 'Dificultad')

    def clean_seguimiento(self):
        return self.validate_range(self.cleaned_data.get('seguimiento'), 'Seguimiento')

    def validate_range(self, value, field_name):
        if value is None or not (0 <= value <= 10):
            raise ValidationError(f'{field_name} debe ser un valor entre 0 y 10.')
        return value

    def storePublicacion(self):
        cleaned_data = self.cleaned_data

        materia = get_object_or_404(Materia, id=cleaned_data.pop('materia'))
        profesor = get_object_or_404(Profesor, id=cleaned_data.pop('profesor'))
        usuario = get_object_or_404(User, id=self.usuario)

        return Publicacion.objects.create(
            usuario=usuario,
            materia=materia,
            profesor=profesor,
            **cleaned_data
        )