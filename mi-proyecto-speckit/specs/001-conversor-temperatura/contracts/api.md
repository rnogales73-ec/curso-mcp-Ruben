# Contract: Python API & CLI Conversor de Temperatura

## 1. Función General

```python
def convertir_temperatura(valor: Union[int, float, str], origen: str, destino: str) -> float:
    """
    Convierte un valor de temperatura entre escalas 'C', 'F' o 'K'.
    
    Arroja:
        ValueError: Si el valor no es numérico, si la escala es inválida, 
                    o si una temperatura en Kelvin es menor a 0.
    """
```

## 2. Funciones de Conversión Directa

- `celsius_a_fahrenheit(c: Union[int, float, str]) -> float`
- `fahrenheit_a_celsius(f: Union[int, float, str]) -> float`
- `celsius_a_kelvin(c: Union[int, float, str]) -> float`
- `kelvin_a_celsius(k: Union[int, float, str]) -> float`
- `fahrenheit_a_kelvin(f: Union[int, float, str]) -> float`
- `kelvin_a_fahrenheit(k: Union[int, float, str]) -> float`

## 3. Interfaz de Línea de Comandos (CLI)

Ejecución interactiva mediante:
`uv run python conversor_temperatura.py`
Proporciona opciones de menú numérico (1 a 4 y 0 para salir).
