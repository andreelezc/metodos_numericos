# Método de Interpolación Lineal

from sympy import *
from sympy.plotting import plot
from termcolor import cprint

# Función f(x)
x = symbols('x')
f = x ** 3 - x ** 2 + 2


# Evalúa la función en x = x
def res(funcion, valor):
    return funcion.subs(x, valor)


# Aproxima la raíz de f(x) con un error (tolerancia) Epsilon
def interpolacion(p_a, p_b, tolerancia):
    i = 1
    c = p_a

    if res(f, p_a) * res(f, p_b) >= 0:
        cprint('Error: ', color='red', attrs=['bold'], end="")
        print('Los valores f(a) y f(b) tienen el mismo signo. Modifique el intervalo.\n')
        return

    print(f'\n{"i":<5} {"X₀":<12} {"X₁":<12} {"Xn+1":<12} {"f(Xn+1)":<12} {"Error":<12}')
    while abs((p_b - p_a)) > tolerancia:

        # Calcula Xn+1
        c = (p_a * res(f, p_b) - p_b * res(f, p_a)) / (res(f, p_b) - res(f, p_a))
        f_c = res(f, c)

        # Verifica si c es raíz
        if f_c == 0 or abs(f_c) < tolerancia:
            break

        # Modifica el intervalo de acuerdo al signo de f(c).
        if res(f, a) * f_c > 0:
            p_a = c
        else:
            p_b = c

        print(f'{i:<5} {str("%.4f" % p_a):<12} {str("%.4f" % p_b):<12} {str("%.4f" % c):<12} {str("%.4f" % f_c):<12} {str("%.4f" % abs(p_b - p_a)):<12}')
        i = i + 1
    cprint("El valor de la raíz es:  %.4f" % c, color='green', attrs=['bold'])


# Ingreso de Datos

cprint('{: ^100}'.format(" MÉTODO DEL INTERPOLACIÓN LINEAL "), 'blue', attrs=['bold'], end="\n")
print('Función: ', latex(f))

a = float(input('\nExtremo inferior del intervalo: '))  # -2
b = float(input('Extremo superior del intervalo: '))  # 3
epsilon = float(input('Epsilon: '))

interpolacion(a, b, epsilon)
plot(f, (x, a, b), title='Método de Interpolación Lineal \n', line_color='orange')
