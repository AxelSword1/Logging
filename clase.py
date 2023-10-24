import logging

class Calculadora:
    def suma(a, b):
        result = a + b
        #Este es un logging de nivel INFO 
        logging.info(f'Suma: {a} + {b} = {result}')
        return result

    def resta(a, b):
        result = a - b
        logging.info(f'Resta: {a} - {b} = {result}')
        return result

    def multiplicacion(a, b):
        result = a * b
        logging.info(f'Multiplicación: {a} * {b} = {result}')
        return result

    def division(a, b):
        if b == 0:
            #Este es un logging de nivel ERROR 
            logging.error("¡Error! No se puede dividir entre cero.")
            return "¡Error! No se puede dividir entre cero."
        else:
            result = a / b
            logging.info(f'División: {a} / {b} = {result}')
            return result
