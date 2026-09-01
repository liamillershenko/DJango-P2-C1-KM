"""
Capa de datos de EcoEnergy.

Esta fase no usa Models ni ORM: los datos viven en archivos JSON dentro
de /data. Este módulo concentra la carga, validación y las operaciones
sobre esas colecciones, para que las Views solo coordinen y las
Templates solo presenten (responsabilidades MVT separadas).
"""
import json

from django.conf import settings

ARCHIVO_ZONAS = "zonas.json"
ARCHIVO_CATEGORIAS = "categorias.json"
ARCHIVO_DISPOSITIVOS = "dispositivos.json"


def cargar_json(nombre_archivo):
    """Carga un archivo JSON desde /data y valida que sea una lista.

    Se ejecuta en cada solicitud a propósito: así, si el docente
    modifica temporalmente el archivo durante la revisión (CA-06, CA-09),
    la aplicación refleja el cambio sin reiniciar el servidor ni tocar
    código.
    """
    ruta = settings.DATA_DIR / nombre_archivo
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)

    if not isinstance(datos, list):
        raise ValueError(f"{nombre_archivo} debe contener una lista de registros")

    return datos


def obtener_zonas():
    """Retorna todas las zonas registradas."""
    return cargar_json(ARCHIVO_ZONAS)


def obtener_categorias():
    """Retorna todas las categorías registradas."""
    return cargar_json(ARCHIVO_CATEGORIAS)


def obtener_dispositivos():
    """Retorna todos los dispositivos registrados."""
    return cargar_json(ARCHIVO_DISPOSITIVOS)


def buscar_por_id(coleccion, identificador):
    """Retorna el primer registro cuyo id coincide, o None si no existe."""
    return next(
        (item for item in coleccion if item.get("id") == identificador),
        None,
    )


def dispositivos_de_zona(zona_id, dispositivos):
    """Filtra los dispositivos que pertenecen a una zona específica."""
    return [d for d in dispositivos if d.get("zona_id") == zona_id]


def calcular_consumo_total(dispositivos):
    """Suma el consumo (kWh) de una colección de dispositivos."""
    return round(sum(d.get("consumo_kwh", 0) for d in dispositivos), 2)


def calcular_estado(consumo_total, limite_kwh):
    """Determina el estado de una zona según su límite (CA-05)."""
    return "ALERTA" if consumo_total > limite_kwh else "NORMAL"


def enriquecer_dispositivos(dispositivos, categorias):
    """Agrega el nombre de categoría a cada dispositivo, para presentarlo.

    Si categoria_id no referencia una categoría existente, el
    dispositivo igual se muestra (no rompe la interfaz) con una
    etiqueta explícita en vez de fallar.
    """
    enriquecidos = []
    for dispositivo in dispositivos:
        categoria = buscar_por_id(categorias, dispositivo.get("categoria_id"))
        enriquecidos.append(
            {
                **dispositivo,
                "categoria_nombre": categoria["nombre"] if categoria else "Sin categoría",
            }
        )
    return enriquecidos


def resumen_zona(zona, dispositivos_zona):
    """Calcula cantidad, consumo total y estado de una zona (CA-04)."""
    consumo_total = calcular_consumo_total(dispositivos_zona)
    estado = calcular_estado(consumo_total, zona.get("limite_kwh", 0))
    return {
        "cantidad_dispositivos": len(dispositivos_zona),
        "consumo_total": consumo_total,
        "estado": estado,
    }
