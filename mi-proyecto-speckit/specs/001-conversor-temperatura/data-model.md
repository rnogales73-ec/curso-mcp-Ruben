# Data Model: Conversor de Temperatura

## Entidades y Tipos

### 1. Escala
- **Valores posibles**: `"CELSIUS"`, `"FAHRENHEIT"`, `"KELVIN"`
- **Alias válidos**: `"C"`, `"F"`, `"K"`
- **Reglas**: Inmune a mayúsculas/minúsculas y espacios en blanco al inicio/final.

### 2. LecturaTermica
- **valor**: `float` (o representable como número flotante; cadenas numéricas son casteadas).
- **escala**: Cadena identificadora de la escala.

### 3. Matriz de Conversiones Válidas
- `(CELSIUS, FAHRENHEIT)`: `(C * 9/5) + 32`
- `(CELSIUS, KELVIN)`: `C + 273.15`
- `(FAHRENHEIT, CELSIUS)`: `(F - 32) * 5/9`
- `(FAHRENHEIT, KELVIN)`: `(F - 32) * 5/9 + 273.15`
- `(KELVIN, CELSIUS)`: `K - 273.15`
- `(KELVIN, FAHRENHEIT)`: `(K - 273.15) * 9/5 + 32`
- `(ESCALA_X, ESCALA_X)`: Retorna el mismo valor numérico.
