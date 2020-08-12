# Método de Newton Raphson para aproximar raíces de ecuaciones

from sympy import *
from sympy.plotting import plot
from termcolor import cprint


# Función f(x)
x = symbols('x')
f = -0.0013 * x ** 3 + 0.3 * x ** 2 + 8 * x - 372
# f = 2*x**3 - 3


# Primera y segunda derivada de f(x)
der1 = diff(f)
der2 = diff(der1)


# Evalúa una función en x = valor
def res(funcion, valor):
    return funcion.subs(x, valor)


def fourier(p_a, p_b):
    """
    Verifica las Leyes de Fourier para la convergencia del método.
    p_a: Extremo inferior del intervalo
    p_b: Extremo superior del intervalo
    :return: Valor inicial Xo
    """

    # f(a) * f(b) < 0
    if res(f, p_a) * res(f, p_b) >= 0:
        cprint('Error: ', color='red', attrs=['bold'], end="")
        print('Los valores f(a) y f(b) tienen el mismo signo. Modifique el intervalo.\n')
        return
    else:
        # f'(x) != 0
        if der1 == 0:
            print('F\'(x) es nula. Modifique la función.')
            return
        else:
            # f(Xo) * f''(Xo) > 0
            if res(f, p_a) * res(der2, p_a) > 0:
                x_0 = p_a
            elif res(f, p_b) * res(der2, p_b) > 0:
                x_0 = p_b
            else:
                return
    return x_0


def newton_raphson(x_0, tolerancia):
    print(f'\n{"X₀":<12} {"X₁":<12} {"Error":<12}')

    # Itera hasta hallar raíz
    while True:
        x1 = x_0 - res(f, x_0) / res(der1, x_0)
        e = abs(x1 - x_0)

        print(f'{str("%.4f" % x_0):<12} {str("%.4f" % x1):<12} {str("%.4f" % abs(x1 - x_0)):<12}')

        if e < tolerancia or res(f, x_0) == 0:
            break
        x_0 = x1
    return '\nRaiz = ' + '{:.6f}'.format(x_0)


# Ingreso de Datos

cprint('{: ^100}'.format(" MÉTODO DE NEWTON RAPHSON "), 'blue', attrs=['bold'], end="\n")
print('Función: ', latex(f))


a = 24
b = 26
# a = 1.0
# b = 1.9
epsilon = 10 ** (-3)

x0 = fourier(a, b)

if x0 is not None:
    cprint('\n✅ ', color='green', attrs=['bold'], end="")
    print('La función cumple todas las condiciones de Fourier')
    print('\nIntervalo inicial: [' + str(a) + ', ' + str(b) + ']')
    print('X₀ = ', x0)
    cprint(newton_raphson(x0, epsilon), color='green', attrs=['bold'])
    plot(f, (x, a, b), title='Método de Newton Raphson\n', line_color='orange')

else:
    cprint('Error: ', color='red', attrs=['bold'], end="")
    print('No se pudo definir Xo')

