"""URLs de la app zonas."""
from django.urls import path

from . import views

app_name = "zonas"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("zonas/", views.listado_zonas, name="listado"),
    path("zonas/<int:zona_id>/", views.detalle_zona, name="detalle"),
]
