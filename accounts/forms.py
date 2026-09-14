from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario


class FormularioRegistro(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["username", "email", "password1", "password2"]


class FormularioLogin(AuthenticationForm):
    pass
