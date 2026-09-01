"""
Configuración del proyecto EcoEnergy.

Base generada según el flujo enseñado en Unidad 1 (startproject config .)
y ajustada para la Fase 1 de la Evaluación Sumativa I · TI3041.

Alcance de esta fase: no se solicitan Models, migraciones ni ORM. La
"base de datos" del sistema son los archivos JSON ubicados en /data.
"""

from pathlib import Path

# Construye rutas dentro del proyecto de esta forma: BASE_DIR / "subruta"
BASE_DIR = Path(__file__).resolve().parent.parent

# ADVERTENCIA DE SEGURIDAD: clave de desarrollo. No usar en producción real.
SECRET_KEY = "django-insecure-ecoenergy-fase1-cambia-esta-clave-en-produccion"

# ADVERTENCIA DE SEGURIDAD: no ejecutar con DEBUG=True en producción real.
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Aplicación de Django
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Paquete externo justificado en ANALISIS.md: genera el markup de
    # Bootstrap 5 (CSS/JS y helpers de formulario) desde Templates Django.
    "django_bootstrap5",
    # Aplicación propia del caso EcoEnergy
    "zonas",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Carpeta de plantillas compartida en la raíz del proyecto.
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Esta fase no persiste datos en base de datos (no se solicitan Models ni
# ORM). Se mantiene una configuración SQLite mínima solo porque Django la
# exige para ejecutar comandos de gestión como `manage.py check`.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "es-cl"
TIME_ZONE = "America/Santiago"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Carpeta donde viven los archivos JSON usados como fuente de datos de
# EcoEnergy (zonas.json, categorias.json, dispositivos.json).
DATA_DIR = BASE_DIR / "data"
