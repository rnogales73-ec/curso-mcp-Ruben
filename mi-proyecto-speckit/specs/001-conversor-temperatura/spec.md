# Feature Specification: Conversor de Temperatura

**Feature Branch**: `001-conversor-temperatura`

**Created**: 2026-09-03

**Status**: Ready for Planning

**Input**: User description: "Implementa conversor_temperatura siguiendo el spec: clase-sdd/spec_manual.md. Ayudame Configurando el Tema de Python con uv"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Conversión Bidireccional entre Celsius y Fahrenheit (Priority: P1)

Como usuario, quiero convertir un valor de temperatura de grados Celsius a Fahrenheit y viceversa, para interpretar valores térmicos en los dos sistemas de medida más comunes con precisión de dos decimales.

**Why this priority**: Es la conversión más habitual en aplicaciones prácticas y constituye el núcleo esencial del conversor.

**Independent Test**: Puede validarse de manera aislada convirtiendo valores conocidos (ej. 0 °C -> 32 °F, 100 °C -> 212 °F, -40 °C -> -40 °F) y verificando que el resultado sea numérico y con 2 decimales.

**Acceptance Scenarios**:

1. **Given** una temperatura válida en Celsius (ej. 0 °C), **When** se solicita la conversión a Fahrenheit, **Then** el sistema devuelve 32.00 °F.
2. **Given** una temperatura válida en Fahrenheit (ej. 212 °F), **When** se solicita la conversión a Celsius, **Then** el sistema devuelve 100.00 °C.
3. **Given** una temperatura negativa válida (ej. -40 °C o -40 °F), **When** se convierte a la escala opuesta, **Then** el sistema procesa el cálculo sin error y devuelve -40.00.

---

### User Story 2 - Conversión Bidireccional entre Celsius y Kelvin (Priority: P2)

Como usuario técnico o científico, quiero convertir una temperatura entre Celsius y Kelvin garantizando que se respeten los límites termodinámicos naturales (cero absoluto).

**Why this priority**: Esencial para contextos científicos y educativos donde la escala absoluta Kelvin es el estándar internacional.

**Independent Test**: Se valida independientemente convirtiendo valores conocidos (ej. 0 °C -> 273.15 K) y confirmando el rechazo inmediato de temperaturas Kelvin inferiores a 0.

**Acceptance Scenarios**:

1. **Given** una temperatura de 0 °C, **When** se convierte a Kelvin, **Then** el resultado es exactamente 273.15 K.
2. **Given** una temperatura de 373.15 K, **When** se convierte a Celsius, **Then** el resultado es 100.00 °C.
3. **Given** un valor en Kelvin menor a 0 (ej. -1 K o -0.5 K), **When** se intenta la conversión, **Then** el sistema rechaza la operación informando un error explícito.

---

### User Story 3 - Conversión entre Fahrenheit y Kelvin y Misma Escala (Priority: P3)

Como usuario, quiero poder convertir directamente entre Fahrenheit y Kelvin, y que si selecciono la misma escala de entrada y salida, el sistema conserve el valor original.

**Why this priority**: Proporciona completitud a la matriz de conversión entre las 3 escalas sin requerir transformaciones intermedias manuales.

**Independent Test**: Conversión de 32 °F a Kelvin (273.15 K) y verificación de identidad (ej. 25 °C a Celsius devuelve 25.00 °C).

**Acceptance Scenarios**:

1. **Given** una temperatura de 32 °F, **When** se convierte a Kelvin, **Then** el resultado es 273.15 K.
2. **Given** un valor en cualquier escala válida (ej. 25.5 en Celsius), **When** se solicita convertir a la misma escala (Celsius), **Then** el sistema retorna el mismo valor redondeado a dos decimales (25.50).

---

### Edge Cases

- **Entrada no numérica**: Cuando el usuario suministra un texto no numérico (ej. "abc", "", None), el sistema debe reportar un error descriptivo y claro indicando que el valor no es convertible a número, evitando cierres no controlados.
- **Valores por debajo del cero absoluto**: Cualquier temperatura inferior al cero absoluto correspondiente a su escala (-273.15 °C, -459.67 °F, o < 0 K) debe ser rechazada explícitamente.
- **Identidad de escala**: Si escala origen y destino son idénticas, se retorna el valor redondeado a 2 decimales sin realizar transformaciones intermedias.
- **Números negativos válidos**: Temperaturas negativas en Celsius y Fahrenheit (por encima del cero absoluto) deben ser aceptadas y procesadas con exactitud.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: El sistema DEBE permitir convertir temperaturas entre las tres escalas: Celsius (C), Fahrenheit (F) y Kelvin (K).
- **FR-002**: El sistema DEBE redondear los resultados finales a exactamente 2 posiciones decimales.
- **FR-003**: El sistema DEBE rechazar cualquier entrada en la escala Kelvin con un valor menor a 0 K emitiendo un mensaje de error claro.
- **FR-004**: El sistema DEBE rechazar entradas con valores no numéricos mediante mensajes de error claros y controlados.
- **FR-005**: El sistema DEBE devolver el mismo valor numérico si la escala de origen y destino coinciden.
- **FR-006**: El sistema DEBE aceptar y procesar números negativos válidos en Celsius y Fahrenheit.
- **FR-007**: El entorno del proyecto DEBE gestionarse de forma determinista mediante `uv` (declarado en `pyproject.toml` con Python >= 3.13) y permitir la ejecución de pruebas automatizadas mediante `uv run pytest`.

### Key Entities

- **LecturaTermica**: Representa una medición de temperatura, compuesta por un valor numérico continuo (`valor`) y su unidad o escala de medida asociada (`escala`).
- **EscalaTemperatura**: Tipo o conjunto admitido con los tres dominios soportados: `CELSIUS`, `FAHRENHEIT`, `KELVIN`.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: El 100% de las conversiones descritas en la matriz (C<->F, C<->K, F<->K y misma escala) producen resultados matemáticamente exactos redondeados a 2 decimales.
- **SC-002**: El 100% de los intentos con Kelvin < 0 y valores no numéricos arrojan excepciones controladas con mensajes descriptivos.
- **SC-003**: El 100% de la suite de pruebas automatizadas se ejecuta satisfactoriamente en menos de 2 segundos mediante el comando `uv run pytest`.
- **SC-004**: El entorno y dependencias del proyecto se instalan y resuelven en un solo paso reproducible usando `uv`.

## Assumptions

- La convención para el cero absoluto se establece en: 0 K, -273.15 °C y -459.67 °F.
- Las escalas se reconocen tanto por nombre completo (ej. "Celsius") como por inicial (ej. "C"), sin importar mayúsculas o minúsculas.
- No se requiere persistencia en base de datos; la funcionalidad se ofrece como biblioteca modular y/o interfaz de consola interactiva.
