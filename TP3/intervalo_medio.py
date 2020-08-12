# Método del intervalo medio para hallar raíces de ecuaciones.

from termcolor import cprint
from sympy import *
from sympy.plotting import plot
from mpmath import log

# Función f(x)
x = symbols('x')
f = x ** 3 - x ** 2 + 2


# Evalúa la función en x = x
def res(funcion, valor):
    return funcion.subs(x, valor)


# Aproxima la raíz de f(x) con un error (tolerancia) Epsilon
def intervalo_medio(p_a, p_b, tolerancia):
    if res(f, p_a) * res(f, p_b) >= 0:
        cprint('Error: ', color='red', attrs=['bold'], end="")
        print('Los valores f(a) y f(b) tienen el mismo signo. Modifique el intervalo.\n')
        return

    c = p_a
    i = 1

    print(f'\n{"i":<5} {"X₀":<12} {"X₁":<12} {"Xn+1":<12} {"f(Xn+1)":<12} {"Error":<12}')
    while abs((p_b - p_a)) >= tolerancia:

        # Calcula Xn+1
        c = (p_a + p_b) / 2

        # Chequea si el punto calculado es raíz.
        if res(f, c) == 0.0:
            break

        # Modifica el intervalo de acuerdo al signo de f(c).
        if res(f, c) * res(f, p_a) < 0:
            p_b = c
        else:
            p_a = c

        print(f'{i:<5} {str("%.4f" % p_a):<12} {str("%.4f" % p_b):<12} {str("%.4f" % c):<12} {str("%.4f" % res(f, c)):<12} {str("%.4f" % abs(p_b - p_a)):<12}')
        i = i + 1

    cprint("\nEl valor de la raíz es:  %.4f" % c, color='green', attrs=['bold'])


def iteraciones(cota_error):
    n = (log(b-a) - log(cota_error))/log(2)
    return ceiling(n)

# Ingreso de datos

cprint('{: ^100}'.format(" MÉTODO DEL INTERVALO MEDIO "), 'blue', attrs=['bold'], end="\n")
print('Función: ', latex(f))

a = float(input('\nExtremo inferior del intervalo: '))  # -2
b = float(input('Extremo superior del intervalo: '))  # 3
epsilon = float(input('Epsilon: '))

print('Cantidad de iteraciones necesarias: ', iteraciones(epsilon))
cprint('\nIntervalo inicial: [' + str(a) + ', ' + str(b) + ']', attrs=['bold'])

intervalo_medio(a, b, epsilon)
p = plot(f, (x, a, b), title='Método del Intervalo Medio\n', line_color='orange')
