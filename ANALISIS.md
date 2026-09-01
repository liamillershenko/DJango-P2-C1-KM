# ANALISIS.md · EcoEnergy Fase 1

## 1. Relaciones y multiplicidades

Basado en el modelo UML del informe de evaluación:

```
Zona (1) ──contiene──> (0..*) Dispositivo (0..*) ──clasifica──> (1) Categoria
```

- Una **Zona** puede tener cero o muchos **Dispositivos** (`0..*`); un
  Dispositivo pertenece exactamente a una Zona (`1`).
- Un **Dispositivo** pertenece exactamente a una **Categoria** (`1`); una
  Categoria puede clasificar cero o muchos Dispositivos (`0..*`).
- Las relaciones se implementan mediante identificadores en los archivos
  JSON, no mediante Models ni ORM (fuera del alcance de esta fase).

## 2. Claves de conexión

| Archivo             | Clave primaria | Claves foráneas (referencian)         |
| -------------------- | --------------- | ---------------------------------------- |
| `zonas.json`          | `id`             | —                                          |
| `categorias.json`     | `id`             | —                                          |
| `dispositivos.json`   | `id`             | `zona_id` → `zonas.id`, `categoria_id` → `categorias.id` |

La resolución de relaciones se centraliza en `zonas/services.py`:
`buscar_por_id()` resuelve una relación por id, y `dispositivos_de_zona()`
filtra dispositivos por `zona_id`. Ninguna vista ni template recorre los
JSON directamente.

## 3. Matriz Criterio de aceptación | Archivo/Componente | Prueba

| Criterio | Archivo / Componente                                         | Prueba realizada                                                                 |
| -------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| CA-01    | `zonas/views.py::listado_zonas`, `templates/zonas/listado.html`  | `GET /zonas/` muestra las 4 zonas presentes en `zonas.json`.                          |
| CA-02    | `zonas/services.py::resumen_zona`, `templates/zonas/listado.html`| Cada tarjeta de zona muestra nombre, límite, cantidad de dispositivos y botón "Ver detalle". |
| CA-03    | `zonas/views.py::detalle_zona`, `templates/zonas/detalle.html`   | `GET /zonas/1/` muestra dispositivos, categoría, consumo y estado de la zona.         |
| CA-04    | `zonas/services.py` (`calcular_consumo_total`, `resumen_zona`)   | Las cantidades y sumas se calculan en Python; ningún número está escrito en el HTML.  |
| CA-05    | `zonas/services.py::calcular_estado`                             | Zona 2 (consumo 330 > límite 300) muestra ALERTA; zonas 1 y 3 muestran NORMAL.        |
| CA-06    | `zonas/services.py::cargar_json` (lectura en cada solicitud)     | Se agregaron dispositivos válidos a `dispositivos.json` y aparecieron sin tocar código. |
| CA-07    | `templates/zonas/detalle.html` (bloque `{% else %}`)             | Zona 4 (sin dispositivos en `dispositivos.json`) muestra mensaje y sigue operativa.    |
| CA-08    | `zonas/views.py::detalle_zona` (`raise Http404`)                 | `GET /zonas/999/` responde 404 con `templates/404.html`.                              |
| CA-09    | `templates/base.html` (navegación fija, sin datos "hardcodeados")| Al duplicar registros la navegación y estructura se mantienen intactas.               |
| CA-10    | `static/zonas/css/estilos.css` (`.tabla-scroll`)                 | La tabla de dispositivos usa `overflow-y: auto` dentro de un contenedor con alto máximo. |
| CA-11    | `templates/base.html`, `templates/zonas/*.html`                  | Header, nav, tarjetas, tablas y botones comparten la misma paleta y jerarquía tipográfica. |
| CA-12    | `static/zonas/css/estilos.css` (`.badge-normal`, `.badge-alerta`)| Los estados siempre incluyen texto ("NORMAL"/"ALERTA") e ícono, no solo color.         |
| CA-13    | Proyecto completo                                                 | `python manage.py check` se ejecuta sin errores desde un clon limpio del repositorio. |

## 4. Decisiones de diseño relevantes

- **Capa de servicios separada de las Views** (`services.py`): concentra
  carga, validación y cálculos, dejando las Views enfocadas en coordinar
  la solicitud y armar el contexto (principio de responsabilidad única,
  alineado con MVT).
- **Lectura de JSON en cada solicitud** en lugar de cargarlo una vez al
  iniciar el servidor: permite que el docente modifique los archivos
  durante la revisión y la aplicación refleje el cambio sin reiniciar.
- **`enriquecer_dispositivos()`** agrega el nombre de categoría a cada
  dispositivo antes de llegar al Template, para que este solo presente
  datos ya resueltos y no tenga que buscar relaciones.
- **Zona sin dispositivos incluida a propósito** en los datos de ejemplo
  (`zonas.json`, id 4) para dejar demostrado el caso CA-07 sin depender
  de que el docente lo genere manualmente.
