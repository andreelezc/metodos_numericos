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
        t.add_column('∇' + str(i).translate(sup) + 'Y', tabla[::, i])
    print(t)


# Calcular u
def calcular_u(valor_u, termino):
    aux = valor_u
    for i in range(1, termino):
        aux = aux * (valor_u - i)
    return aux


# Aplicar fórmula
def formula(vector_x, vector_y, n):
    suma = vector_y[-1]
    u = (valor - vector_x[-1]) / (vector_x[1] - vector_x[0])
    for i in range(1, n):
        suma = suma + (calcular_u(u, i) * tabla_dif[n-(i+1)][i]) / math.factorial(i)
    return suma


# Resultados
cprint('{: ^80}'.format(" NEWTON GREGORY "), 'blue', attrs=['bold'], end="\n")
cprint('{: ^80}'.format(" Descendente "), 'red', attrs=['bold'], end="\n")

# Ingreso de vectores X e Y
x = list(map(float, input('Ingrese valores de X:').split()))  # [15, 25, 35, 45, 55, 65]
y = list(map(float, input('Ingrese valores de Y:').split()))  # [0.965926, 0.906308, 0.819152, 0.707107, 0.573576, 0.422618]

# Valor a interpolar
valor = float(input('Valor a interpolar: '))  # 60

# Cantidad de términos a usar (depende de la longitud de Y)
cant_term = len(y)

# Tabla de Diferencias
tabla_dif = calcular_diferencias(y)
print('{: ^80}'.format('Tabla de Diferencias\n'))
imprimir(tabla_dif, x, y)

resultado = formula(x, y, cant_term)
print("\nF(x = " + str(valor) + "): {:g}".format(resultado))
