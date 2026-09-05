## Resultados del conversor
=============================================
       CONVERSOR DE TEMPERATURA
=============================================
1. Celsius    -> Fahrenheit y Kelvin
2. Fahrenheit -> Celsius y Kelvin
3. Kelvin     -> Celsius y Fahrenheit
4. Conversión personalizada (C, F, K)
0. Salir
=============================================

Seleccione una opción (0-4): 1
Ingrese grados Celsius (°C): -10
Ingrese grados Celsius (°C): -10
-> 14.00 °F
-> 263.15 K

Seleccione una opción (0-4): 2
Ingrese grados Fahrenheit (°F): veite y cinco
[Error]: Valor no numérico o inválido para temperatura: 'veite y cinco'.

Seleccione una opción (0-4):
Seleccione una opción (0-4): 4
Ingrese el valor numérico: 20
Escala origen (C / F / K): C
Escala destino (C / F / K): C
-> 20.00 C


 Se ha ejecutado la fase de especificación /speckit.specify para la funcionalidad del conversor de temperatura y la
  configuración con uv.
  ──────
  ### Reporte de Finalización (Completion Report)
  • Directorio de la Feature: 001-conversor-temperatura
  • Archivo de Especificación: spec.md
  • Lista de Verificación de Calidad: requirements.md
  ──────
  ### Resumen de la Especificación
  1. Historias de Usuario Priorizadas:
      • P1: Conversión bidireccional entre Celsius y Fahrenheit con redondeo a 2 decimales y soporte de valores negativos
      válidos.
      • P2: Conversión bidireccional entre Celsius y Kelvin con restricción termodinámica estricta (K ≥ 0).
      • P3: Conversión entre Fahrenheit y Kelvin, y manejo de identidad de escala (misma escala de origen y destino).
  2. Casos Borde & Validación Defensiva:
      • Detección y manejo de entradas no numéricas (e.g. "abc") arrojando errores descriptivos y controlados.
      • Rechazo explícito de cualquier valor inferior a 0  K (y equivalentes por debajo del cero absoluto).
  3. Restricciones del Entorno:
      • Gestión estricta de entorno virtual y dependencias con uv (Python ≥3.13).
      • Pruebas automatizadas con pytest ejecutadas mediante uv run pytest.

  ──────
  ### Estado del Checklist de Calidad

  • Calidad de Contenido: Superado (100% enfocado en necesidades y libre de detalles de implementación en historias de usuario).
  • Completitud de Requerimientos: Superado (sin marcadores [NEEDS CLARIFICATION] pendientes).
  • Disponibilidad para Planificación: Listo para /speckit.plan.

  ### Diferencia entre spec_manual.md y el spec.md generado
  - el spec.md implementa 3 historias de usuario
  - Implementa casos de borde -> que también lo implementa el spec_manual.md
  - Implementa Requerimientos funcionales
  - Define entidades claves
  - Define criterios de exito como: Medidas de salida, asume 

  ## Implementación
  ### /speckit.implement
  #### 4. Validación de Calidad y Pruebas
  Ejecución de test_conversor.py mediante uv run pytest -v:

    test_conversor.py::test_celsius_fahrenheit_bidireccional PASSED          [ 14%]
    test_conversor.py::test_celsius_kelvin_bidireccional PASSED              [ 28%]
    test_conversor.py::test_redondeo_dos_decimales PASSED                    [ 42%]
    test_conversor.py::test_rechazo_kelvin_menor_cero PASSED                 [ 57%]
    test_conversor.py::test_caso_borde_valor_no_numerico PASSED              [ 71%]
    test_conversor.py::test_caso_borde_mismo_valor_origen_destino PASSED     [ 85%]
    test_conversor.py::test_caso_borde_numeros_negativos_validos PASSED      [100%]

    ============================== 7 passed in 0.09s ==============================

  El ciclo completo de Spec-Driven Development (SDD) ha finalizado con éxito.

  =============================================
       CONVERSOR DE TEMPERATURA
=============================================
1. Celsius    -> Fahrenheit y Kelvin
2. Fahrenheit -> Celsius y Kelvin
3. Kelvin     -> Celsius y Fahrenheit
4. Conversión personalizada (C, F, K)
0. Salir
=============================================

Seleccione una opción (0-4): 1
Ingrese grados Celsius (°C): 25
-> 77.00 °F
-> 298.15 K

Seleccione una opción (0-4):

Seleccione una opción (0-4): 2
Ingrese grados Fahrenheit (°F): veinte y cinco grados
[Error]: Valor no numérico o inválido para temperatura: 'veinte y cinco grados'.

Seleccione una opción (0-4): 

Seleccione una opción (0-4): 4
Ingrese el valor numérico: 25
Escala origen (C / F / K): c
Escala destino (C / F / K): c
-> 25.00 C

Seleccione una opción (0-4): 