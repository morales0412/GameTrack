from django.forms import ModelForm
from .models import Game
from django import forms


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ["nombre", "descripcion", "genero", "plataforma", "ano_lanzamiento"]
        labels = {
            "ano_lanzamiento": "Año de lanzamiento",
        }
        widgets = {"ano_lanzamiento": forms.DateInput(attrs={"type": "date"})}
