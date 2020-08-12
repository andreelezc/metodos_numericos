import numpy as np
import math
from sympy import *
from prettytable import PrettyTable
from TP2.Errores import *


# def truncate(number, digits) -> float:
#     stepper = 10.0 ** digits
#     return math.trunc(stepper * number) / stepper
#
#
# def tres(numero):
#     """
#     Trunca el número a 3 dígitos en total.
#     """
#     resultado = 0.0
#     num = math.trunc(numero)
#     if num < 10:
#         resultado = truncate(numero, 2)
#     elif 10 < num < 100:
#         resultado = truncate(numero, 1)
#     elif num >= 100:
#         resultado = math.trunc(numero)
#     return resultado


x = symbols('x')
polinomio = x ** 3 - 6 * x ** 2 + 3 * x - 0.149
valor_real = np.polyval([1, -6, 3, -0.149], 4.71)

tabla = [['Exacto', 4.71, 22.1841, 104.487111, 133.1046, 14.13],
         ['Truncado', 4.71, 22.1, 104, 132, 14.1],
         ['Redondeado', 4.71, 22.2, 105, 133, 14.1]]

t = PrettyTable()
t.field_names = ['', 'x', 'x²', 'x3', '6x²', '3x']
for fila in tabla:
    t.add_row(fila)

p_truncado = math.ceil(-0.149 + tabla[1][5] + tabla[1][3] - tabla[1][4])
e_abs_truncado = error_absoluto(5, valor_real, p_truncado)
e_rel_truncado = error_relativo(5, valor_real, p_truncado)

p_redondeado = math.floor(-0.149 + tabla[2][5] + tabla[2][3] - tabla[2][4])
e_abs_red = error_absoluto(5, valor_real, p_redondeado)
e_rel_red = error_relativo(5, valor_real, p_redondeado)

res = PrettyTable()
res.add_column('Valor', ['Truncado', 'Redondeado'])
res.add_column('Error Absoluto', [e_abs_truncado, e_abs_red])
res.add_column('Error Relativo', [e_rel_truncado, e_rel_red])

print('P[X] =', latex(polinomio))
print('P[4.71] =', valor_real)
print(t)

print('\nValor Truncado:', p_truncado, '\tValor Redondeado:', p_redondeado)
print(res)
