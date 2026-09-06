from conversor_temperatura import convertir_temperatura

def test_flujo_completo_conversion():
    # El flujo completo (pedir conversión → validar entrada → devolver resultado) debe funcionar de punta a punta con una entrada válida
    # Entrada inicial: 25 en Celsius hacia Kelvin
    entrada_valor = "25"
    escala_origen = "C"
    escala_destino = "K"
    
    # Proceso de validación y cálculo
    resultado = convertir_temperatura(entrada_valor, escala_origen, escala_destino)
    
    # Salida esperada final
    assert resultado == 298.15
