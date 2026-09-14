from django.urls import path
from .views import RegistroUsuario, InicioSesionUsuario, CierreSesionUsuario

urlpatterns = [
    path("registro/", RegistroUsuario.as_view(), name="registro"),
    path("login/", InicioSesionUsuario.as_view(), name="login"),
    path("logout/", CierreSesionUsuario.as_view(), name="logout"),
]
