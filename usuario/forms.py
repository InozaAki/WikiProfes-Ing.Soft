from django import forms
from django.contrib.auth.models import User

class RegistroForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    confirmationPassword = forms.CharField()

    def clean(self):
        
        password = self.cleaned_data.get('password')
        confirmationPassword = self.cleaned_data.get('password2')

        if password != confirmationPassword:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return super().clean()

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