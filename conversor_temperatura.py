"""
Módulo: conversor_temperatura.py
Descripción: Conversor entre escalas de temperatura (Celsius, Fahrenheit, Kelvin)
             siguiendo la especificación definida en clase-sdd/spec_manual.md.
"""

from typing import Union

# Constantes de referencia
CERO_ABSOLUTO_K = 0.0
CERO_ABSOLUTO_C = -273.15
CERO_ABSOLUTO_F = -459.67

ESCALAS_VALIDAS = {"CELSIUS", "FAHRENHEIT", "KELVIN", "C", "F", "K"}
MAPA_ESCALAS = {
    "C": "CELSIUS",
    "CELSIUS": "CELSIUS",
    "F": "FAHRENHEIT",
    "FAHRENHEIT": "FAHRENHEIT",
    "K": "KELVIN",
    "KELVIN": "KELVIN",
}


def _normalizar_escala(escala: str) -> str:
    """Normaliza y valida el identificador de escala."""
    if not isinstance(escala, str):
        raise ValueError(f"La escala debe ser de tipo texto, se recibió: {type(escala).__name__}")
    escala_limpia = escala.strip().upper()
    if escala_limpia not in MAPA_ESCALAS:
        raise ValueError(f"Escala '{escala}' no válida. Use Celsius ('C'), Fahrenheit ('F') o Kelvin ('K').")
    return MAPA_ESCALAS[escala_limpia]


def _validar_valor(valor: Union[int, float, str]) -> float:
    """Valida y castea el valor a float manejando valores no numéricos con un error claro."""
    if isinstance(valor, bool):
        raise ValueError("El valor de temperatura no puede ser booleano.")
    try:
        return float(valor)
    except (ValueError, TypeError):
        raise ValueError(f"Valor no numérico o inválido para temperatura: '{valor}'.")


# ==========================================
# Funciones específicas de conversión
# ==========================================

def celsius_a_fahrenheit(c: Union[int, float, str]) -> float:
    """Convierte grados Celsius a Fahrenheit redondeado a 2 decimales."""
    c_val = _validar_valor(c)
    if c_val < CERO_ABSOLUTO_C:
        raise ValueError(f"Temperatura inválida: {c_val} °C está por debajo del cero absoluto ({CERO_ABSOLUTO_C} °C).")
    return round((c_val * 9.0 / 5.0) + 32.0, 2)


def fahrenheit_a_celsius(f: Union[int, float, str]) -> float:
    """Convierte grados Fahrenheit a Celsius redondeado a 2 decimales."""
    f_val = _validar_valor(f)
    if f_val < CERO_ABSOLUTO_F:
        raise ValueError(f"Temperatura inválida: {f_val} °F está por debajo del cero absoluto ({CERO_ABSOLUTO_F} °F).")
    return round((f_val - 32.0) * 5.0 / 9.0, 2)


def celsius_a_kelvin(c: Union[int, float, str]) -> float:
    """Convierte grados Celsius a Kelvin redondeado a 2 decimales."""
    c_val = _validar_valor(c)
    k_val = c_val + 273.15
    if k_val < CERO_ABSOLUTO_K:
        raise ValueError(f"Temperatura inválida: {c_val} °C resulta en {k_val:.2f} K (por debajo de 0 K).")
    return round(k_val, 2)


def kelvin_a_celsius(k: Union[int, float, str]) -> float:
    """Convierte Kelvin a grados Celsius redondeado a 2 decimales."""
    k_val = _validar_valor(k)
    if k_val < CERO_ABSOLUTO_K:
        raise ValueError(f"Temperatura rechazada: {k_val} K es menor que 0 K (cero absoluto).")
    return round(k_val - 273.15, 2)


def fahrenheit_a_kelvin(f: Union[int, float, str]) -> float:
    """Convierte grados Fahrenheit a Kelvin redondeado a 2 decimales."""
    f_val = _validar_valor(f)
    k_val = (f_val - 32.0) * 5.0 / 9.0 + 273.15
    if k_val < CERO_ABSOLUTO_K:
        raise ValueError(f"Temperatura inválida: {f_val} °F resulta en {k_val:.2f} K (por debajo de 0 K).")
    return round(k_val, 2)


def kelvin_a_fahrenheit(k: Union[int, float, str]) -> float:
    """Convierte Kelvin a grados Fahrenheit redondeado a 2 decimales."""
    k_val = _validar_valor(k)
    if k_val < CERO_ABSOLUTO_K:
        raise ValueError(f"Temperatura rechazada: {k_val} K es menor que 0 K (cero absoluto).")
    return round((k_val - 273.15) * 9.0 / 5.0 + 32.0, 2)


# ==========================================
# Función genérica de conversión
# ==========================================

def convertir_temperatura(valor: Union[int, float, str], origen: str, destino: str) -> float:
    """
    Convierte una temperatura entre escalas ('CELSIUS', 'FAHRENHEIT', 'KELVIN' o 'C', 'F', 'K').

    Criterios de la spec:
    - Convierte correctamente de Celsius a Fahrenheit y viceversa
    - Convierte correctamente de Celsius a Kelvin y viceversa
    - Redondea el resultado a 2 decimales
    - Rechaza una temperatura en Kelvin menor a 0
    - Valor no numérico como entrada produce error claro (ValueError descriptivo)
    - Mismo valor de entrada y salida devuelve el mismo número (redondeado a 2 decimales)
    - Números negativos válidos en Celsius/Fahrenheit se procesan sin problema
    """
    num = _validar_valor(valor)
    origen_norm = _normalizar_escala(origen)
    destino_norm = _normalizar_escala(destino)

    # Validar que si el origen es Kelvin, no sea menor a 0
    if origen_norm == "KELVIN" and num < CERO_ABSOLUTO_K:
        raise ValueError(f"Temperatura rechazada: {num} K es menor que 0 K (cero absoluto).")

    # Mismo valor de entrada y salida
    if origen_norm == destino_norm:
        return round(num, 2)

    rutas = {
        ("CELSIUS", "FAHRENHEIT"): celsius_a_fahrenheit,
        ("CELSIUS", "KELVIN"): celsius_a_kelvin,
        ("FAHRENHEIT", "CELSIUS"): fahrenheit_a_celsius,
        ("FAHRENHEIT", "KELVIN"): fahrenheit_a_kelvin,
        ("KELVIN", "CELSIUS"): kelvin_a_celsius,
        ("KELVIN", "FAHRENHEIT"): kelvin_a_fahrenheit,
    }

    funcion_conversion = rutas.get((origen_norm, destino_norm))
    if not funcion_conversion:
        raise ValueError(f"Conversión de '{origen}' a '{destino}' no soportada.")

    return funcion_conversion(num)


# ==========================================
# Interfaz de Línea de Comandos (CLI)
# ==========================================

def main():
    print("=" * 45)
    print("       CONVERSOR DE TEMPERATURA")
    print("=" * 45)
    print("1. Celsius    -> Fahrenheit y Kelvin")
    print("2. Fahrenheit -> Celsius y Kelvin")
    print("3. Kelvin     -> Celsius y Fahrenheit")
    print("4. Conversión personalizada (C, F, K)")
    print("0. Salir")
    print("=" * 45)

    while True:
        try:
            opcion = input("\nSeleccione una opción (0-4): ").strip()

            if opcion == "0":
                print("¡Hasta luego!")
                break
            elif opcion == "1":
                c = input("Ingrese grados Celsius (°C): ")
                print(f"-> {celsius_a_fahrenheit(c):.2f} °F")
                print(f"-> {celsius_a_kelvin(c):.2f} K")
            elif opcion == "2":
                f = input("Ingrese grados Fahrenheit (°F): ")
                print(f"-> {fahrenheit_a_celsius(f):.2f} °C")
                print(f"-> {fahrenheit_a_kelvin(f):.2f} K")
            elif opcion == "3":
                k = input("Ingrese Kelvin (K): ")
                print(f"-> {kelvin_a_celsius(k):.2f} °C")
                print(f"-> {kelvin_a_fahrenheit(k):.2f} °F")
            elif opcion == "4":
                val = input("Ingrese el valor numérico: ")
                orig = input("Escala origen (C / F / K): ").strip()
                dest = input("Escala destino (C / F / K): ").strip()
                res = convertir_temperatura(val, orig, dest)
                print(f"-> {res:.2f} {dest.upper()}")
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError as e:
            print(f"[Error]: {e}")
        except (KeyboardInterrupt, EOFError):
            print("\nOperación finalizada.")
            break


if __name__ == "__main__":
    main()
