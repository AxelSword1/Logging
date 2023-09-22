from clase import Calculadora


def test_multiplicacion():
    assert Calculadora.multiplicacion(3,4) == 12
