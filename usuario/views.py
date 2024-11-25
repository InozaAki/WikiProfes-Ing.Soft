from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegistroForm

# Create your views here.
class RegistroView(generic.FormView):
    template_name = ''
    form_class = RegistroForm
    success_url = reverse_lazy('')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        usuario = form.storeUser()
        #Usuario utilizadfo en login en el futuro
        return super().form_valid(form)