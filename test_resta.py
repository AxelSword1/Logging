import logging
from clase import Calculadora

# Configura la configuración de logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def test_resta():
    assert Calculadora.resta(10,5) == 5

if __name__ == "__main__":
    test_resta()
