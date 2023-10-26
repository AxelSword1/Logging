#libreria de logging
import logging
from clase import Calculadora

# Configura el logging de lo que quieres mandar
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def test_suma():
    assert Calculadora.suma(3,5) == 8

if __name__ == "__main__":
    test_suma()
