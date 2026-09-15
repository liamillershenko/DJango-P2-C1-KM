# IA.md · Declaración de uso de Inteligencia Artificial

## Herramienta utilizada

Claude (Anthropic), a través de la interfaz de chat de Claude.ai.

## Contexto entregado a la IA

Se entregaron el enunciado oficial de la Evaluación Sumativa I · Fase 1
(EcoEnergy, TI3041) y el material de las Clases 2 a 6 de la Unidad 1
(entorno Django/Git, URLs y Views, Templates y contexto, JSON y paquetes
externos, integración MVT). No se entregó ningún dato ni credencial
personal.

## Qué se generó con apoyo de IA

Este proyecto fue construido con una asistencia de IA amplia, no acotada
a una sola parte: estructura del proyecto Django (`config/`, `zonas/`),
`services.py` para cargar y procesar los JSON, `views.py` y `urls.py`,
los tres archivos `zonas.json` / `categorias.json` / `dispositivos.json`
de ejemplo, los Templates (`base.html`, `inicio.html`, `listado.html`,
`detalle.html`, `404.html`), los estilos propios (`estilos.css`) y la
documentación (`README.md`, `ANALISIS.md`, este archivo).

## Verificación aplicada antes de esta entrega

- Se compiló cada archivo `.py` (`python -m py_compile`) para descartar
  errores de sintaxis.
- Se validó que los tres JSON son sintácticamente válidos.
- Se simuló manualmente la lógica de `resumen_zona()` (consumo total y
  estado NORMAL/ALERTA) contra los datos de ejemplo, confirmando que la
  Zona 2 queda en ALERTA (330 > 300) y el resto en NORMAL, incluida la
  zona sin dispositivos.
- **No fue posible ejecutar `python manage.py runserver` ni
  `python manage.py check`** en el entorno donde se generó este
  proyecto, porque no cuenta con Django instalado ni acceso a internet
  para instalarlo.

## Responsabilidad pendiente del estudiante

El enunciado es explícito: *"el estudiante debe seleccionar, adaptar,
integrar y probar la respuesta"* y *"copiar una salida sin comprenderla
o sin verificarla no constituye evidencia de logro"*. Además, la Fase 2
se rinde presencialmente, **sin IA**, modificando esta misma base.

Antes de entregar, el estudiante debe, con su propio entorno (`.venv`
activo):

1. Ejecutar `python manage.py check` y confirmar que no hay errores.
2. Ejecutar `python manage.py runserver` y navegar `/`, `/zonas/` y
   varias rutas `/zonas/<id>/`, incluida una que no exista (404).
3. Leer `services.py` y `views.py` línea por línea hasta poder explicar,
   sin apoyo, qué hace cada función y por qué.
4. Ajustar nombres, comentarios o estructura si algo no refleja cómo
   el estudiante entiende o explicaría su propio proyecto.
5. Reemplazar esta sección con sus propias pruebas y capturas/resultados
   reales antes de registrar el commit de entrega.

