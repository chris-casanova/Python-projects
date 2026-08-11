import sys
sys.path.insert(0, '.')

from experimentos.retotaxi.reto_taxi import calcular_tarifa

def test_fin_de_semana():
    # Arrange
    hora = 12
    dia = "domingo"
    llueve = False
    distancia_km = 7
    zona = "normal"

    # Act
    resultado = calcular_tarifa(hora, dia, llueve, distancia_km, zona)

    # Assert
    assert resultado["tarifa_final"] == 37.38