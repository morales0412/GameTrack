from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Game
from django.urls import reverse_lazy
from .forms import GameForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ListarJuegos(LoginRequiredMixin, ListView):
    model = Game
    template_name = "games/listar_juegos.html"
    context_object_name = "juegos"

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda)
        return queryset


class DetalleJuego(LoginRequiredMixin, DetailView):
    model = Game
    template_name = "games/detalle_juego.html"
    context_object_name = "juego"


class CrearJuego(LoginRequiredMixin, CreateView):
    model = Game
    form_class = GameForm
    template_name = "games/crear_juego.html"
    success_url = reverse_lazy("listar_juegos")


class ActualizarJuego(LoginRequiredMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = "games/actualizar_juego.html"
    success_url = reverse_lazy("listar_juegos")


class EliminarJuego(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = reverse_lazy("listar_juegos")
