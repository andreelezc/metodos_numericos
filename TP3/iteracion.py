# Método de iteración para hallar raíces de ecuaciones de la forma x = g(x)

from sympy import *
from sympy.plotting import plot
from termcolor import cprint

init_printing()

x = symbols('x')

# Función f(x)
f = 2 * x ** 2 - 11 * x + 5

# Función g(x) despejada
g = sqrt((11*x - 5)/2)


# Evalúa una función en x = x
def res(funcion, valor):
    return funcion.subs(x, valor)


def iteracion(func, xo, tol, n):
    print(f'\n{"i":<12} {"X₁":<12} {"Error":<12}')

    # Itera hasta N o hasta hallar raíz
    for i in range(1, n+1):
        x1 = res(func, xo)
        if abs(x1 - xo) < tol:
            return 'Raíz = ' + str("%.4f" % x1)
        print(f'{str(i):<12} {str("%.4f" % x1):<12} {str("%.4f" % abs(x1 - xo)):<12}')
        xo = x1
    return "\nEl método falló después de {} iteraciones".format(n)


# Ingreso de Datos

cprint('{: ^100}'.format(" MÉTODO DE ITERACIÓN "), 'blue', attrs=['bold'], end="\n")
cprint('Función f(x): ', attrs=['bold'])
pprint(f)
cprint('Función g(x): ', attrs=['bold'])
pprint(g)

x0 = float(input('\nX₀ = '))  # 1
N = int(input('Nº máximo de iteraciones: '))
epsilon = 0.0001

cprint(iteracion(g, x0, epsilon, N), attrs=['bold'])
plot(f, (x, -5, 5), title='Método de Iteración\n', line_color='orange')
