import logging
class Calculadora:
    def suma(a, b):
        result = a + b
        logging.info(f'Suma: {a} + {b} = {result}')
        logging.debug(f'Debug: Realizando suma de {a} + {b}')
        if result < 100:
            logging.warning(f'Advertencia: La suma de {a} + {b} es menor que 100')
        if result > 0:
            logging.critical(f'Crítico: Suma diferente a cero en {a} + {b}')
        if result != 0:
            logging.error(f'Error: Resultado positivo en la suma de {a} + {b}') 
     
        return result

    def resta(a, b):
        result = a - b
        logging.info(f'Resta: {a} - {b} = {result}')
        logging.debug(f'Debug: Realizando resta de {a} - {b}')
        if result < 0:
            logging.warning(f'Advertencia: La resta de {a} - {b} es negativa')        
        if result != 0:
            logging.error(f'Error: Resultado diferente a cero en la resta de {a} - {b}')
        if result < -100:
            logging.critical(f'Crítico: Resta menor que -100 en {a} - {b}')
        return result

    def multiplicacion(a, b):
        result = a * b
        logging.info(f'Multiplicación: {a} * {b} = {result}')
        logging.debug(f'Debug: Realizando multiplicación de {a} * {b}')
        if result < 1000:
            logging.warning(f'Advertencia: El resultado de la multiplicación es menor que 1000')        
        if result > 0:
            logging.error(f'Error: Resultado positivo en la multiplicación de {a} * {b}')        
        if result != 0:
            logging.critical(f'Crítico: Multiplicación diferente a cero en {a} * {b}')
        return result

    def division(a, b):
        if b == 0:
            logging.error("¡Error! No se puede dividir entre cero.")
            return "¡Error! No se puede dividir entre cero."
        else:
            result = a / b
            logging.info(f'División realizada: {a} / {b} = {result}')        
            logging.debug(f'Debug: Realizando división de {a} / {b}')        
            if result < 100:
                logging.warning(f'Advertencia: El resultado de la división es menor que 100')        
            if result > 0:
                logging.error(f'Error: Resultado positivo en la división de {a} / {b}')        
            if result != 0:
                logging.critical(f'Crítico: División diferente a cero en {a} / {b}')
        
            return result
