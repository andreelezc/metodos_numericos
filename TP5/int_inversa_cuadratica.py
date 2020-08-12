import numpy as np
import math
from prettytable import PrettyTable
from termcolor import cprint


# Calcular tabla de diferencias
def calcular_diferencias(vector_y):
    n = np.shape(vector_y)[0]
    tabla = np.zeros([n, n])  # Crea una matriz cuadrada llena de ceros
    tabla[::, 0] = vector_y  # Primera columna es y
    for j in range(1, n):
        for i in range(n - j):
            # Calculo de diferencias
            tabla[i][j] = (tabla[i + 1][j - 1] - tabla[i][j - 1])
    return tabla


# Imprimir como tabla
def imprimir(tabla, vector_x, vector_y):
    t = PrettyTable()
    t.add_column('X', vector_x)
    t.add_column('Y', vector_y)
    n, m = np.shape(tabla)

    sup = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

    # formato de salida de los números
    for i in range(n):
        for j in range(m):
            tabla[i][j] = "{:g}".format(tabla[i][j])

    for i in range(1, len(tabla)):
        t.add_column('Δ' + str(i).translate(sup) + 'Y', tabla[::, i])
    print(t)


def termino2(tabla, vector_x):
    h = vector_x[1] - vector_x[0]
    t2 = ((tabla[0][2]) / (math.factorial(2) * h**2))
    return t2


def termlineal(tabla, vector_x):
    h = vector_x[1] - vector_x[0]
    tl = (tabla[0][1] / h) - (tabla[0][2] / (math.factorial(2) * (h ** 2)) * vector_x[1]) - \
         ((tabla[0][2] / (math.factorial(2) * h ** 2)) * vector_x[0])
    return tl


def termind(tabla, vector_x, val):
    h = vector_x[1] - vector_x[0]
    ti = (tabla[0][0]) - ((tabla[0][1] / h) * vector_x[0]) + \
         ((tabla[0][2] / (math.factorial(2) * h**2)) * vector_x[0] * vector_x[1]) - val
    return ti


def ecuacion(a, b, c):
    coeff = [a, b, c]
    raices = np.roots(coeff)
    print('x1 = ', "{:g}".format(raices[0]))
    print('x2 = ', "{:g}".format(raices[1]))


# Resultados
cprint('{: ^80}'.format(" INTERPOLACIÓN INVERSA CUADRÁTICA "), 'blue', attrs=['bold'], end="\n")

# Ingreso de vectores X e Y
x = list(map(float, input('Ingrese valores de X:').split()))  # [0.5, 0.6, 0.7, 0.8, 0.9, 10]; [15, 25, 35, 45, 55, 65]
y = list(map(float, input('Ingrese valores de Y:').split()))  # [0.479426, 0.564642, 0.644218, 0.717356, 0.783327, 0.841471] # [0.965926, 0.906308, 0.819152, 0.707107, 0.573576, 0.422618]

# Valor a interpolar
valor = float(input('Valor a interpolar: '))  # 0.5; 0.946285

# Tabla de Diferencias
tabla_dif = calcular_diferencias(y)

# Calculo de los terminos
t_a = termino2(tabla_dif, x)
t_b = termlineal(tabla_dif, x)
t_c = termind(tabla_dif, x, valor)

print('{: ^80}'.format('Tabla de Diferencias\n'))
imprimir(tabla_dif, x, y)
ecuacion(t_a, t_b, t_c)
