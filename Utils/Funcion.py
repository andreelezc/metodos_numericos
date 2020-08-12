from sympy import *


def convertir_a_funcion(s):
    """
    Código para convertir un string ingresado por el usuario a una función
    parametrizable y evaluable.
    :param s: string con la fórmula de la función
    :return: función evaluable
    """

    # Separa en dos elementos (a y b) el string recibido por el signo "="
    a, b = s.split("=", 1)

    # El primer miembro de la ecuación [f(x, y)] representa los parámetros
    args = sympify(a).args

    # El segundo miembro de la ecuación (la fórmula) es la función propiamente dicha
    f = sympify(b)

    # Crea la función a partir de los elementos anteriores
    def f_func(*passed_args):
        argumentos = dict(zip(args, passed_args))
        resultado = f.subs(argumentos)
        return float(resultado)
    return f_func
