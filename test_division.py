import logging
from clase import Calculadora

# Configura la configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def test_division():
    assert Calculadora.division(12,0) == 4

if __name__ == "__main__":
    test_division()
