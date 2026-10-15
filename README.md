# Práctico 3 — Automatización de Calidad y Blindaje

Proyecto de Python utilizado para configurar controles automáticos, ejecutar pruebas y documentar una auditoría de calidad.

## Archivos

- `ventas.py`: función de autorización de ventas.
- `test_ventas.py`: cuatro pruebas unitarias.
- `.githooks/pre-commit`: controles de formato, linter y pruebas antes de cada commit.

## Preparación en Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install ruff coverage
git config core.hooksPath .githooks
```

## Verificación

```powershell
python -m unittest discover -v
python -m coverage run --branch --source=ventas -m unittest discover -v
python -m coverage report -m
ruff format --check .
ruff check .
```

El pre-commit hook ejecuta secuencialmente formato, linter y pruebas. Si un control falla, Git cancela ese commit.