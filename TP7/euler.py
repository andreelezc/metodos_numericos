from termcolor import cprint
from Utils.Funcion import convertir_a_funcion

sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


# Formula de Euler
def euler(x0, y0, h, fin):

    # Itera hasta el valor "fin"
    i = 0
    while x0 < fin:
        print('X' + str(i).translate(sub) + ' = ' + "%.2f" % x0 + ' Y' + str(i).translate(sub) + ' = ' + "%.6f" % y0)
        x0 = x0 + h
        y0 = y0 + func(x0, y0) * h
        i = i + 1


cprint('{: ^80}'.format(" MÉTODO DE EULER "), 'blue', attrs=['bold'], end="\n")

# Ingreso de datos
funcion = (input('Ingrese la función:'))  # ("f(x, y) = ... ") x + y + x*y
func = convertir_a_funcion(funcion)

x_0 = int(input('X₀ = '))  # 0
y_0 = int(input('Y₀ = '))  # 1
inc = float(input('h = '))  # 0.025
x_final = float(input('Xn = '))  # 0.1

print('\nResultados')
euler(x_0, y_0, inc, x_final)
