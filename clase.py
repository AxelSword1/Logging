class Calculadora:
    def suma(a, b):
        return a + b

    def resta(a, b):
        return a - b

    def multiplicacion(a, b):
        return a * b

    def division(a, b):
        if b == 0:
            return "¡Error! No se puede dividir entre cero."
        else:
            return a / b
