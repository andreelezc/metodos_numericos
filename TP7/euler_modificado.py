from termcolor import cprint
from Utils.Funcion import convertir_a_funcion

sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


# Predice el valor de Y usando el método de Euler
def predicho(x, y, h):
    p_y = y + h * func(x, y)
    return p_y


# Corrige el valor predicho
def corregido(x_ant, y_ant, x1, y1, h):
    epsilon = 0.00001
    ult_corr = y1

    while abs(ult_corr - y1) > epsilon:
        y1 = ult_corr
        ult_corr = y_ant + ((func(x_ant, y_ant) + func(x1, y1)) / 2) * h

    return ult_corr


def euler_mod(x0, y0, xn, h):
    i = 0
    while x0 <= xn:
        x1 = x0 + h
        p_y = predicho(x0, y0, h)
        c_y = corregido(x0, y0, x1, p_y, h)
        x0 = x1
        y0 = c_y
        i += 1
        print('X' + str(i).translate(sub) + ' = ' + "%.2f" % x0 + ' Y' + str(i).translate(sub) + ' = ' + "%.6f" % y0)


cprint('{: ^80}'.format(" MÉTODO DE EULER MODIFICADO"), 'blue', attrs=['bold'], end="\n")

# Ingreso de Datos
funcion = (input('Ingrese la función:'))  # ("f(x, y) = ... ") x**2 + y**2
func = convertir_a_funcion(funcion)

x_0 = int(input('X₀ = '))  # 0
y_0 = int(input('Y₀ = '))  # 1
inc = float(input('h = '))  # 0.2
x_final = float(input('Xn = '))  # 0.6

print('\nResultados:')
euler_mod(x_0, y_0, x_final, inc)
