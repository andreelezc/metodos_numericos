# Método de Tanteo para separar intervalos en donde hay raíces.

import numpy as np
from prettytable import PrettyTable
from termcolor import cprint
from sympy import *
from sympy.plotting import plot

# Variable simbólica h
h = symbols('h')

# Coeficientes del polinomio, en orden.
# f = np.poly1d([-0.0013, 0.3, 8, -372])

# Función f(x)
f = -0.0013 * h ** 3 + 0.3 * h ** 2 + 8 * h - 372


def tanteo():
    """
    Compara los signos de valores adyacentes de Y. Si son distintos, guarda los
    valores en xo y x1 respectivamente para informar el intervalo.
    :return: Intervalo donde la función cambia de signo.
    """
    x0 = 0
    x1 = 0
    for i in range(len(y) - 1):
        if np.sign(y[i]) != np.sign(y[i + 1]):
            x0 = x[i]
            x1 = x[i + 1]
            print('Hay raíz en el intervalo [' + str(x0) + ', ' + str(x1) + ']')
            plot(f, (h, a, b), title='Método de Tanteos\n', line_color='orange')

    if x0 == 0 and x1 == 0:
        print('No se hallaron raíces en el intervalo con el incremento ΔX = ' + str(inc))


# Ingreso de Datos

cprint('{: ^100}'.format(" MÉTODO DE TANTEO "), 'blue', attrs=['bold'], end="\n")
print('Función:\n', f)

a = float(input('\nExtremo inferior del intervalo: '))  # 24
b = float(input('Extremo superior del intervalo: '))  # 26
inc = float(input('Incremento (ΔX): '))

x = np.arange(a, b + inc, inc)
y = []

for item in x:
    # y.append(round(np.polyval(f, x[i]), 3))
    y.append(f.subs(h, item))

tabla = PrettyTable()
tabla.add_column('X', x)
tabla.add_column('Y', y)
print(tabla)

tanteo()
