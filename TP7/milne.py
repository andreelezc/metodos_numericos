import numpy as np
from termcolor import cprint
from Utils.Funcion import convertir_a_funcion


# Runge Kutta de 4to orden para calcular los puntos necesarios
def rk(vy, xo, yo, h):
    for i in range(1, 4):
        k1 = h * f(xo, yo)
        k2 = h * f(xo + h / 2, yo + k1 / 2)
        k3 = h * f(xo + h / 2, yo + k2 / 2)
        k4 = h * f(xo + h, yo + k3)

        vy[i] = yo + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        yo = vy[i]

    return vy


# Ecuación de Predicción y Corrección de Milne
# Predice un valor y lo corrige de forma iterativa
def milne(vx, vy, h, n):
    epsilon = 0.001
    for i in range(3, n - 1):
        p_y = vy[i - 3] + 4 / 3 * h * (2 * f(vx[i], vy[i]) - f(vx[i - 1], vy[i - 1]) + 2 * f(vx[i - 2], vy[i - 2]))
        c_y = vy[i - 1] + h / 3 * (f(vx[i - 1], vy[i - 1]) + 4 * f(vx[i], vy[i]) + f(vx[i], p_y))
        while abs(c_y - p_y) > epsilon:
            p_y = c_y
            c_y = vy[i - 1] + h / 3 * (f(vx[i - 1], vy[i - 1]) + 4 * f(vx[i], vy[i]) + f(vx[i], p_y))
        vy[i+1] = c_y
    return vy


cprint('{: ^80}'.format(" MÉTODO DE MILNE"), 'blue', attrs=['bold'], end="\n")

# Ingreso de datos
f = input('Ingrese la función: ')  # x**2 + y**2
f = convertir_a_funcion(f)

x0 = float(input('Xo = '))  # 0
y0 = float(input('Yo = '))  # 1
xn = float(input('Xn = '))  # 0.8
inc = float(input('h = '))  #0.2


# Vectores X e Y
x = np.arange(x0, xn + inc, inc)
cant = len(x)
y = np.zeros(cant)
y[0] = y0

# Runge Kutta para los primeros 4 puntos
rk(y, x0, y0, inc)
print('\nValores obtenidos con Runge Kutta de 4to. Orden')
print('i  \t\t  X  \t\t Y')
for j in range(4):
    print(j, '\t\t  %.2f' % x[j], '\t\t %.6f' % y[j])

# Milne para los puntos restantes
milne(x, y, inc, cant)
print('\nValores obtenidos con Milne')
print('i  \t\t  X  \t\t Y')
for j in range(4, cant):
    print(j, '\t\t  %.2f' % x[j], '\t\t %.6f' % y[j])
