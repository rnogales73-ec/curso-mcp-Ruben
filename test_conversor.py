import pytest
from conversor_temperatura import (
    convertir_temperatura,
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    celsius_a_kelvin,
    kelvin_a_celsius,
    fahrenheit_a_kelvin,
    kelvin_a_fahrenheit,
)

def test_celsius_fahrenheit_bidireccional():
    # 0 °C = 32 °F
    assert celsius_a_fahrenheit(0) == 32.0
    assert fahrenheit_a_celsius(32) == 0.0
    # 100 °C = 212 °F
    assert celsius_a_fahrenheit(100) == 212.0
    assert fahrenheit_a_celsius(212) == 100.0

def test_celsius_kelvin_bidireccional():
    # 0 °C = 273.15 K
    assert celsius_a_kelvin(0) == 273.15
    assert kelvin_a_celsius(273.15) == 0.0
    # 25 °C = 298.15 K
    assert celsius_a_kelvin(25) == 298.15
    assert kelvin_a_celsius(298.15) == 25.0

def test_redondeo_dos_decimales():
    # 37 °C a °F: (37 * 9/5) + 32 = 98.6
    assert convertir_temperatura(37, "C", "F") == 98.6
    # 35.555 °C a Kelvin: 35.555 + 273.15 = 308.705 -> 308.7 o 308.71
    resultado = convertir_temperatura(35.555, "C", "K")
    assert len(str(resultado).split(".")[-1]) <= 2

def test_rechazo_kelvin_menor_cero():
    with pytest.raises(ValueError, match="menor.*0"):
        kelvin_a_celsius(-1)
    with pytest.raises(ValueError, match="menor.*0"):
        kelvin_a_fahrenheit(-0.5)
    with pytest.raises(ValueError, match="menor.*0"):
        convertir_temperatura(-5, "K", "C")

def test_caso_borde_valor_no_numerico():
    with pytest.raises(ValueError, match="no numérico|inválido"):
        convertir_temperatura("abc", "C", "F")
    with pytest.raises(ValueError, match="no numérico|inválido"):
        celsius_a_fahrenheit("xyz")

def test_caso_borde_mismo_valor_origen_destino():
    assert convertir_temperatura(25.5, "Celsius", "Celsius") == 25.5
    assert convertir_temperatura(100, "F", "F") == 100.0
    assert convertir_temperatura(300.123, "K", "K") == 300.12

def test_caso_borde_numeros_negativos_validos():
    # -40 °C == -40 °F
    assert convertir_temperatura(-40, "C", "F") == -40.0
    assert convertir_temperatura(-40, "F", "C") == -40.0
    # -10 °C a Kelvin -> 263.15 K
    assert convertir_temperatura(-10, "C", "K") == 263.15
