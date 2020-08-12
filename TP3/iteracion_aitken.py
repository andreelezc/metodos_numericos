# Método de iteración para hallar raíces de ecuaciones de la forma x = g(x)
# acelerando la convergencia con el Cuadrado de Aitken

from sympy import *
from termcolor import cprint

x = symbols('x')

# Función f(x)
f = 100 * x ** 3 + 59 * x ** 2 - 145 * x + 2

# Función g(x) despejada
g = ((-59 * x ** 2 + 145 * x - 2) / 100) ** (1 / 3)


# Evalúa una función en x = x
def res(funcion, valor):
    return funcion.subs(x, valor)


# Fórmula de Aitken
def acelerar(xo, x1, x2):
    return (xo * x2 - x1 * x1) / (xo + x2 - 2 * x1)


# Iteración con Aitken
def iter_aitken(func, xo, tol):
    i = 0
    s = []  # vector que contiene los puntos iniciales para Aitken
    while True:
        xn = res(func, xo)
        s.append(xo)
        print(f'X{i} {str("%.4f" % s[i])}')
        i += 1
        if len(s) == 3:
            r = acelerar(s[0], s[1], s[2])
            print('Aceleración = ', str("%.4f" % r), '\n')
            i = 0  # reinicia el índice
            s = []  # se vacía el vector para cargar otros tres puntos
        if abs(xn - xo) < tol:
            break
        xo = xn
    return 'Raíz = ' + str(xn)


# Ingreso de Datos

cprint('{: ^100}'.format(" MÉTODO DE ITERACIÓN - ACELERACIÓN DE AITKEN"), 'blue', attrs=['bold'], end="\n")
cprint('Función f(x): ', attrs=['bold'])
pprint(f)
cprint('Función g(x): ', attrs=['bold'])
pprint(g)

x0 = 0.5
epsilon = 0.0001

cprint(iter_aitken(g, x0, epsilon), attrs=['bold'])
plot(f, (x, -2, 3), title='Iteración - Aceleración de Aitken\n', line_color='orange')
