# Segundo Orden de Newton

from sympy import *
from sympy.plotting import plot
from termcolor import cprint

pi = 3.14

# Función f(x)
x = symbols('x')
f = (2 / 3) * pi * x ** 3 + 30 * pi * x ** 2 + - 15000

# Primera y segunda derivada de f(x)
der1 = diff(f)
der2 = diff(der1)


# Evalúa una función en x = x
def res(funcion, valor):
    return funcion.subs(x, valor)


# def xo(p_a, p_b):
#     # Define un valor inicial a partir de la semisuma del intervalo
#     x_0 = (p_a + p_b) / 2
#     return x_0


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


def newton_raphson_2(x_0, tolerancia):
    print(f'\n{"X₀":<12} {"X₁":<12} {"Error":<12}')

    # Itera hasta hallar raíz
    while True:
        num = res(f, x_0)
        den = (res(der1, x_0) - ((res(der2, x0) * res(f, x_0)) / (2 * res(der1, x_0))))
        x1 = x_0 - (num / den)
        e = abs(x1 - x_0)

        print(f'{str("%.4f" % x_0):<12} {str("%.4f" % x1):<12} {str("%.4f" % abs(x1 - x_0)):<12}')

        if e < tolerancia or res(f, x_0) == 0:
            break
        x_0 = x1
    return '\nRaiz = ' + '{:.6f}'.format(x_0)


# Ingreso de Datos

cprint('{: ^100}'.format(" SEGUNDO ORDEN DE NEWTON "), 'blue', attrs=['bold'], end="\n")
print('Función: ', latex(f))

a = 10
b = 15
epsilon = 0.001

x0 = fourier(a, b)

if x0 is not None:
    cprint('\n✅ ', color='green', attrs=['bold'], end="")
    print('La función cumple todas las condiciones de Fourier')
    print('\nIntervalo inicial: [' + str(a) + ', ' + str(b) + ']')
    print('X₀ = ', x0)
    cprint(newton_raphson_2(x0, epsilon), color='green', attrs=['bold'])
    plot(f, (x, a, b), title='Segundo Orden de Newton\n', line_color='orange')
else:
    cprint('Error: ', color='red', attrs=['bold'], end="")
    print('No se pudo definir Xo')
