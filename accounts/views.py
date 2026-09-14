from django.shortcuts import render, redirect
from .forms import FormularioRegistro, FormularioLogin
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .models import Usuario

# Create your views here.


class RegistroUsuario(CreateView):
    model = Usuario
    form_class = FormularioRegistro
    template_name = "registration/register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


class InicioSesionUsuario(LoginView):
    model = Usuario
    form_class = FormularioLogin
    template_name = "registration/login.html"


class CierreSesionUsuario(LogoutView):
    pass
