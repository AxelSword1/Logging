import logging
from clase import Calculadora

# Configura la configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def test_multiplicacion():
    assert Calculadora.multiplicacion(3,4) == 12

if __name__ == "__main__":
    test_multiplicacion()