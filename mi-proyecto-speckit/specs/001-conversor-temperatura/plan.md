# Implementation Plan: Conversor de Temperatura

**Branch**: `001-conversor-temperatura` | **Date**: 2026-09-03 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/001-conversor-temperatura/spec.md`

## Summary

Implementar un conversor bidireccional y robusto entre escalas térmicas (Celsius, Fahrenheit, Kelvin) con redondeo a 2 decimales, rechazo de Kelvin < 0, manejo controlado de errores no numéricos y soporte para identidad de escala y valores negativos válidos. La gestión del entorno virtual y dependencias de ejecución/testing se realizará con `uv`.

## Technical Context

**Language/Version**: Python >= 3.13 (definido en `.python-version` y `pyproject.toml`)

**Primary Dependencies**: Estándar de Python (`typing`, `math`), herramientas del ecosistema `uv`

**Storage**: N/A (sin persistencia en base de datos; puramente computacional e interactivo)

**Testing**: `pytest` ejecutado a través de `uv run pytest`

**Target Platform**: Multiplataforma (Windows, Linux, macOS)

**Project Type**: Librería modular con interfaz de línea de comandos (CLI) interactiva

**Performance Goals**: Conversiones instantáneas (<1 ms por cálculo) y suite de pruebas ejecutada en < 2 segundos

**Constraints**: Manejo explícito de excepciones (`ValueError`) con mensajes descriptivos ante entradas no numéricas o físicamente imposibles

**Scale/Scope**: Módulo `conversor_temperatura.py` y suite `test_conversor.py`

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Spec-First**: `spec.md` redactado, validado y checklist completado.
- [x] **Test-First (TDD Mandate)**: Casos de prueba automatizados con `pytest` definidos antes de cerrar la implementación.
- [x] **Python Tooling & Dependency Hygiene via `uv`**: Todas las dependencias declaradas en `pyproject.toml` y ejecutadas mediante comandos `uv run`.
- [x] **Clean Architecture & CLI Explicability**: Funciones puras de cálculo desacopladas de la interacción por consola en `main()`.
- [x] **Defensive Boundary Handling**: Validación exhaustiva de entradas (tipos no numéricos y cotas de cero absoluto).

## Project Structure

### Documentation (this feature)

```text
specs/001-conversor-temperatura/
├── plan.md              # Este archivo
├── research.md          # Investigación y decisiones técnicas
├── data-model.md        # Entidades y tipos
├── quickstart.md        # Guía de ejecución y validación
├── contracts/           # Contrato de la API pública y CLI
└── tasks.md             # Tareas accionables generadas por /speckit-tasks
```

### Source Code (repository root)

```text
conversor_temperatura.py # Módulo principal: funciones matemáticas, validación y CLI
test_conversor.py        # Suite de pruebas unitarias y de casos borde con pytest
pyproject.toml           # Configuración de proyecto y dependencias para uv
```

**Structure Decision**: Estructura de paquete/módulo directa en la raíz del repositorio, alineada a los ejercicios del curso y scripts existentes.

## Complexity Tracking

> No se detectaron violaciones a la constitución. No se requiere justificación de complejidad adicional.

