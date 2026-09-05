# Tasks: Conversor de Temperatura

**Feature**: Conversor de Temperatura | **Branch**: `001-conversor-temperatura` | **Spec**: [spec.md](spec.md) | **Plan**: [plan.md](plan.md)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Verify Python >= 3.13 project configuration in pyproject.toml
- [x] T002 [P] Configure and install pytest as a development dependency using `uv add --dev pytest`
- [x] T003 [P] Verify virtual environment activation and synchronization with `uv sync`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure and validation routines that MUST be complete before user stories

- [x] T004 Define absolute zero constants (`CERO_ABSOLUTO_C`, `CERO_ABSOLUTO_F`, `CERO_ABSOLUTO_K`) in conversor_temperatura.py
- [x] T005 [P] Implement scale normalization and validation helper `_normalizar_escala` in conversor_temperatura.py
- [x] T006 [P] Implement robust numeric parser and validator `_validar_valor` (handling strings and rejecting non-numeric values with clear `ValueError`) in conversor_temperatura.py

**Checkpoint**: Core domain constants and input boundary validation functions are in place.

---

## Phase 3: User Story 1 - Conversión Celsius a Fahrenheit y viceversa (Priority: P1) [MVP]

**Goal**: Permitir conversiones exactas entre Celsius y Fahrenheit con redondeo a 2 decimales y soporte de números negativos válidos.

**Independent Test**: Ejecución de pruebas unitarias para 0 °C -> 32 °F, 100 °C -> 212 °F, 212 °F -> 100 °C y -40 °C -> -40 °F.

### Tests for User Story 1
- [x] T007 [P] [US1] Author unit tests for Celsius <-> Fahrenheit conversions and edge cases in test_conversor.py

### Implementation for User Story 1
- [x] T008 [US1] Implement `celsius_a_fahrenheit` with rounding to 2 decimal places in conversor_temperatura.py
- [x] T009 [US1] Implement `fahrenheit_a_celsius` with rounding to 2 decimal places in conversor_temperatura.py

**Checkpoint**: User Story 1 complete and verifiable independently.

---

## Phase 4: User Story 2 - Conversión Celsius a Kelvin y viceversa (Priority: P2)

**Goal**: Permitir conversiones exactas entre Celsius y Kelvin con redondeo a 2 decimales y rechazo de Kelvin < 0.

**Independent Test**: Convertir 0 °C -> 273.15 K, 25 °C -> 298.15 K, y comprobar que Kelvin < 0 arroja `ValueError`.

### Tests for User Story 2
- [x] T010 [P] [US2] Author unit tests for Celsius <-> Kelvin conversions and negative Kelvin rejection in test_conversor.py

### Implementation for User Story 2
- [x] T011 [US2] Implement `celsius_a_kelvin` with rounding to 2 decimal places and absolute zero validation in conversor_temperatura.py
- [x] T012 [US2] Implement `kelvin_a_celsius` with rounding to 2 decimal places and rejection of Kelvin < 0 in conversor_temperatura.py

**Checkpoint**: User Story 2 complete and verifiable independently.

---

## Phase 5: User Story 3 - Conversión Fahrenheit a Kelvin, Kelvin a Fahrenheit e Identidad de Escala (Priority: P3)

**Goal**: Completar la matriz de conversión permitiendo Fahrenheit <-> Kelvin, misma escala (identidad) y despachador central `convertir_temperatura`.

**Independent Test**: Convertir 32 °F -> 273.15 K, misma escala (ej. 25 °C -> 25 °C), y verificar despacho dinámico.

### Tests for User Story 3
- [x] T013 [P] [US3] Author tests for Fahrenheit <-> Kelvin, same-scale identity, and invalid input strings in test_conversor.py

### Implementation for User Story 3
- [x] T014 [US3] Implement `fahrenheit_a_kelvin` and `kelvin_a_fahrenheit` with rounding to 2 decimal places in conversor_temperatura.py
- [x] T015 [US3] Implement dynamic dispatcher `convertir_temperatura(valor, origen, destino)` handling identity and routes in conversor_temperatura.py

**Checkpoint**: All three user stories functional and unified through `convertir_temperatura`.

---

## Phase 6: Polish & CLI Interface

**Purpose**: Interfaz de usuario interactiva por consola y validación completa del sistema.

- [x] T016 Implement user-friendly interactive CLI `main()` loop with error handling in conversor_temperatura.py
- [x] T017 [P] Execute full test suite via `uv run pytest test_conversor.py` and ensure 100% pass rate
- [x] T018 Verify quickstart validation steps from quickstart.md

---

## Dependencies & Execution Order

- **Phase 1 (Setup)**: Pre-requisito sin dependencias.
- **Phase 2 (Foundational)**: Requiere Phase 1. Bloquea las historias de usuario.
- **Phase 3 (US1)**: Requiere Phase 2. Constituye el MVP.
- **Phase 4 (US2)**: Requiere Phase 2. Independiente de US1.
- **Phase 5 (US3)**: Requiere Phase 2, US1 y US2 para completar la matriz general.
- **Phase 6 (Polish & CLI)**: Requiere todas las fases anteriores.
