"""
Views de la app zonas.

Cada View recibe la solicitud, pide los datos a services.py, calcula lo
mínimo necesario para el contexto y delega toda la presentación al
Template correspondiente (responsabilidades MVT separadas, CA-04).
"""
from django.http import Http404
from django.shortcuts import render

from . import services


def inicio(request):
    """Página de bienvenida con un resumen general del sistema."""
    zonas = services.obtener_zonas()
    dispositivos = services.obtener_dispositivos()

    contexto = {
        "activo": "inicio",
        "total_zonas": len(zonas),
        "total_dispositivos": len(dispositivos),
    }
    return render(request, "zonas/inicio.html", contexto)


def listado_zonas(request):
    """Lista todas las zonas con su resumen de consumo (CA-01, CA-02)."""
    zonas = services.obtener_zonas()
    dispositivos = services.obtener_dispositivos()

    zonas_con_resumen = []
    for zona in zonas:
        dispositivos_zona = services.dispositivos_de_zona(zona["id"], dispositivos)
        resumen = services.resumen_zona(zona, dispositivos_zona)
        zonas_con_resumen.append({**zona, **resumen})

    contexto = {
        "activo": "zonas",
        "zonas": zonas_con_resumen,
    }
    return render(request, "zonas/listado.html", contexto)


def detalle_zona(request, zona_id):
    """Muestra el detalle de una zona: dispositivos, consumo y estado.

    Cubre CA-03, CA-04, CA-05 y CA-07. Si la zona no existe, responde
    con un 404 controlado (CA-08) en lugar de exponer un error técnico.
    """
    zonas = services.obtener_zonas()
    zona = services.buscar_por_id(zonas, zona_id)

    if zona is None:
        raise Http404("La zona solicitada no existe.")

    categorias = services.obtener_categorias()
    dispositivos = services.obtener_dispositivos()

    dispositivos_zona = services.dispositivos_de_zona(zona_id, dispositivos)
    dispositivos_zona = services.enriquecer_dispositivos(dispositivos_zona, categorias)
    resumen = services.resumen_zona(zona, services.dispositivos_de_zona(zona_id, dispositivos))

    contexto = {
        "activo": "zonas",
        "zona": zona,
        "dispositivos": dispositivos_zona,
        **resumen,
    }
    return render(request, "zonas/detalle.html", contexto)
