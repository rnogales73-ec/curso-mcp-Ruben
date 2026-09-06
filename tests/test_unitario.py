import pytest
from conversor_temperatura import convertir_temperatura

def test_convertir_temperatura_celsius_a_fahrenheit():
    # convertir_temperatura: dado 25°C, debe devolver 77°F
    assert convertir_temperatura(25, "C", "F") == 77.0

def test_convertir_temperatura_texto_error():
    # convertir_temperatura: con texto en vez de número, debe dar error claro, no excepción sin control
    with pytest.raises(ValueError, match="no numérico|inválido|no permitido"):
        convertir_temperatura("texto_invalido", "C", "F")

def test_convertir_temperatura_kelvin_negativo():
    # convertir_temperatura: con Kelvin negativo, debe rechazarlo
    with pytest.raises(ValueError, match="menor.*0"):
        convertir_temperatura(-10, "K", "C")
