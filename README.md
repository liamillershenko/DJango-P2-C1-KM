# EcoEnergy · Fase 1

Aplicación Django del lado del servidor para EcoEnergy: permite a pequeñas y
medianas empresas **consultar zonas de consumo energético** y **revisar el
detalle de los dispositivos instalados en cada una**, usando archivos JSON
como fuente de datos.

> Proyecto académico — Programación Back End (TI3041), INACAP.
> Evaluación Sumativa I · Fase 1.

## Requisitos previos

- Python 3.10 o superior
- pip
- Git

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/liamillershenko/DJango-P2-C1-KM.git
cd ecoenergy-backend

# 2. Crear el entorno virtual
python -m venv .venv

# 3. Activar el entorno virtual
# Git Bash:
source .venv/Scripts/activate
# PowerShell:
.\.venv\Scripts\Activate.ps1
# Linux / macOS:
source .venv/bin/activate

# 4. Instalar dependencias
python -m pip install -r requirements.txt

# 5. Verificar la configuración de Django
python manage.py check
```

## Ejecución

```bash
python manage.py runserver
```

Luego abre `http://127.0.0.1:8000/` en el navegador.

## Rutas funcionales

| Ruta                    | Nombre           | Descripción                                   |
| ------------------------ | ---------------- | ---------------------------------------------- |
| `/`                       | `zonas:inicio`    | Página de bienvenida con resumen general.       |
| `/zonas/`                 | `zonas:listado`   | Listado de todas las zonas registradas.         |
| `/zonas/<id>/`            | `zonas:detalle`   | Detalle de una zona: dispositivos y estado.     |

Una ruta `/zonas/<id>/` con un `id` que no existe en `zonas.json` responde
con estado **404** y una página de error propia.

## Estructura del proyecto

```
ecoenergy-backend/
├── manage.py
├── config/            # Configuración global del proyecto (settings, urls)
├── zonas/             # App con la lógica de EcoEnergy
│   ├── services.py    # Carga y procesa los JSON (sin Models/ORM)
│   ├── views.py       # Coordina la solicitud y prepara el contexto
│   └── urls.py
├── templates/
│   ├── base.html       # Layout compartido (header, nav, footer)
│   ├── 404.html         # Página de error para zona inexistente
│   └── zonas/
│       ├── inicio.html
│       ├── listado.html
│       └── detalle.html
├── static/zonas/css/estilos.css
├── data/
│   ├── zonas.json
│   ├── categorias.json
│   └── dispositivos.json
├── requirements.txt
├── ANALISIS.md
└── IA.md
```

## Fuente de datos

No se usan Models ni ORM (fuera del alcance de esta fase). Los datos viven
en `/data` como archivos JSON y se cargan en cada solicitud desde
`zonas/services.py`, por lo que **agregar o modificar registros válidos en
los JSON se refleja de inmediato**, sin tocar código.

| Archivo             | Claves obligatorias                                   |
| -------------------- | ------------------------------------------------------- |
| `zonas.json`          | `id`, `nombre`, `limite_kwh`                              |
| `categorias.json`     | `id`, `nombre`, `descripcion`                             |
| `dispositivos.json`   | `id`, `nombre`, `consumo_kwh`, `zona_id`, `categoria_id`     |

El estado de una zona se calcula dinámicamente:
`ALERTA` si `consumo_total > limite_kwh`, `NORMAL` en caso contrario.

## Dependencia externa

**`django-bootstrap5`** — genera el HTML de Bootstrap 5 (CSS/JS) desde los
Templates mediante `{% bootstrap_css %}` y `{% bootstrap_javascript %}`.
Se usa en `templates/base.html`. Justificación completa en `ANALISIS.md`.

## Pruebas realizadas

- `python manage.py check` sin errores.
- `GET /` → 200, muestra resumen general.
- `GET /zonas/` → 200, lista las 4 zonas con su estado (3 `NORMAL`, 1 `ALERTA`).
- `GET /zonas/1/`, `/zonas/2/`, `/zonas/3/` → 200, detalle con dispositivos.
- `GET /zonas/4/` → 200, zona sin dispositivos, muestra mensaje de colección vacía.
- `GET /zonas/999/` → 404, página de error controlada.
- Se agregaron dispositivos de prueba a `dispositivos.json` y la interfaz
  actualizó cantidades y consumo sin modificar Views ni Templates.
- Verificación visual en ventana angosta (responsive) y con la tabla de
  dispositivos ampliada, comprobando que solo se desplaza la tabla.

## Estado actual y próximos pasos

- **Estado actual:** Fase 1 completa — listado y detalle de zonas
  funcionando sobre JSON, con manejo de casos vacíos y 404.
- **Próximos pasos (fuera del alcance de esta fase):** persistencia con
  Models/ORM, operaciones CRUD, autenticación y permisos, según lo indique
  la Fase 2 o etapas posteriores del curso.
