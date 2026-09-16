from django.db import models


# Create your models here.
class Game(models.Model):
    generos_opciones = [
        ("ACTION", "Acción"),
        ("ADVENTURE", "Aventura"),
        ("RPG", "Rol"),
        ("SHOOTER", "Disparos"),
        ("PUZZLE", "Puzle"),
        ("SIMULATION", "Simulación"),
        ("SPORTS", "Deportes"),
        ("STRATEGY", "Estrategia"),
    ]
    plataformas_opciones = [
        ("PC", "PC"),
        ("PS4", "PlayStation 4"),
        ("PS5", "PlayStation 5"),
        ("XBOX_ONE", "Xbox One"),
        ("XBOX_SERIES_X", "Xbox Series X"),
        ("NINTENDO_SWITCH", "Nintendo Switch"),
        ("MOBILE", "Móvil"),
        ("OTHER", "Otro"),
    ]
    nombre = models.CharField(max_length=100, unique=True, blank=False, null=False)
    descripcion = models.TextField(blank=True)
    genero = models.CharField(
        max_length=20, choices=generos_opciones, blank=False, null=False
    )
    plataforma = models.CharField(
        max_length=20, choices=plataformas_opciones, blank=False, null=False
    )
    ano_lanzamiento = models.DateTimeField(blank=False, null=False)
    creacion_objeto = models.DateTimeField(auto_now_add=True)
