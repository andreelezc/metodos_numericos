from termcolor import cprint
from Utils.Funcion import convertir_a_funcion

sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def rk4(x0, y0, xn, h):
    y = y0
    i = 0
    while x0 <= xn:
        k1 = h * func(x0, y)
        k2 = h * func(x0 + h/2, y + k1/2)
        k3 = h * func(x0 + h/2, y + k2/2)
        k4 = h * func(x0 + h, y + k3)

        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        x0 = x0 + h

        i = i + 1
        print('X' + str(i).translate(sub) + ' = ' + "%.2f" % x0 + ' Y' + str(i).translate(sub) + ' = ' + "%.6f" % y)


cprint('{: ^80}'.format(" MÉTODO DE RUNGE KUTTA 4º ORDEN"), 'blue', attrs=['bold'], end="\n")

# Ingreso de Datos
funcion = (input('Ingrese la función:'))  # ("f(x, y) = ... ") x**2 + y**2
func = convertir_a_funcion(funcion)

x_0 = int(input('X₀ = '))  # 0
y_0 = int(input('Y₀ = '))  # 1
inc = float(input('h = '))  # 0.2
x_n = float(input('Xn = '))  # 0.6

print('\nResultados:')
rk4(x_0, y_0, x_n, inc)
