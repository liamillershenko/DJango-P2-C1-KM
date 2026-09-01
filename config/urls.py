"""URLconf principal del proyecto EcoEnergy."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Toda la funcionalidad del caso EcoEnergy vive en la app "zonas".
    path("", include("zonas.urls")),
]
