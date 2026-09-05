# Research: Conversor de Temperatura

## Decisiones Técnicas

### 1. Manejo de Precisión y Redondeo
- **Decisión**: Uso de aritmética float estándar con llamada final a `round(resultado, 2)`.
- **Razón**: Para temperaturas cotidianas y científicas básicas, la precisión estándar de coma flotante de doble precisión (64 bits) de Python combinada con `round(..., 2)` satisface exactamente la tolerancia exigida sin el overhead de `decimal.Decimal`.
- **Alternativas consideradas**: `decimal.Decimal` (descartado por complejidad innecesaria para un conversor básico de 3 escalas).

### 2. Gestión de Entorno y Dependencias con `uv`
- **Decisión**: Usar `uv` nativo como gestor de paquetes y ejecutor (`uv run`). `pytest` como dependencia en `[project.optional-dependencies]` o sección de desarrollo.
- **Razón**: Máxima velocidad de resolución, compatibilidad total con PEP 517/621 en `pyproject.toml` y cumplimiento estricto de la Constitución del proyecto.
- **Alternativas consideradas**: `pip` directo o `poetry` (descartados para mantener consistencia con el ecosistema moderno `uv`).

### 3. Límites Físicos del Cero Absoluto
- **Decisión**:
  - Kelvin: $0\text{ K}$ (valores menores a 0 provocan `ValueError`).
  - Celsius: $-273.15\text{ }^\circ\text{C}$.
  - Fahrenheit: $-459.67\text{ }^\circ\text{F}$.
- **Razón**: Coherencia termodinámica universal y cumplimiento directo de los criterios de aceptación.
