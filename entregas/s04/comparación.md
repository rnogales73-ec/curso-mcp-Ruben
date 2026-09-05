| Aspecto | Spec a mano | Spec Kit |
|---|---|---|
| ¿Cubrió los mismos casos borde? | Sí: valores no numéricos, temperaturas negativas, conversión a la misma escala y Kelvin menor que 0. | Sí, porque los criterios y casos borde quedaron definidos explícitamente antes de implementar. |
| ¿Qué generó Spec Kit que tú no habías escrito? | No tenía una estructura formal completa. | Generó la especificación, el modelo de datos, el plan, las tareas, el contrato de API y las listas de comprobación. |
| ¿Qué se sintió más rápido de arrancar? | Fue más rápido para comenzar a escribir directamente el código. | Fue más rápido para organizar el proyecto y dividir el trabajo en pasos claros. |
| ¿Cuál te generó más confianza en el resultado? | La prueba manual permitió comprobar rápidamente algunos casos. | Spec Kit generó más confianza porque los requisitos, casos borde y tareas quedaron documentados y verificables. |


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

La proxima vez que tenga un proyecto "de cualquier tamaño" lo realizaré siguiendo todos los pasos estructurados
- speckit.specify
- speckit.plan
- speckit.taks
- speckit.implement