import numpy as np
from prettytable import PrettyTable
from termcolor import cprint


# Calcular tabla de diferencias
def calcular_diferencias(vector_y, vector_x):
    n = np.shape(vector_y)[0]
    tabla = np.zeros([n, n])  # Crea una matriz cuadrada llena de ceros
    tabla[::, 0] = vector_y  # Primera columna es y
    for j in range(1, n):
        for i in range(n - j):
            # Calculo de diferencias
            tabla[i][j] = (tabla[i + 1][j - 1] - tabla[i][j - 1])/(vector_x[i+j] - vector_x[i])
    return tabla


# Imprimir como tabla
def imprimir(tabla, vector_x, vector_y):
    t = PrettyTable()
    t.add_column('X', vector_x)
    t.add_column('Y', vector_y)
    n, m = np.shape(tabla)

    # formato de salida de los números
    for i in range(n):
        for j in range(m):
            tabla[i][j] = "{:g}".format(tabla[i][j])

    for i in range(1, len(tabla)):
        t.add_column('f(' + str('x'*(i+1)) + ')', tabla[::, i])
    print(t)


# Calcular termino producto
def producto(val, i, vector_x):
    prod = 1
    for j in range(i):
        prod = prod * (val - vector_x[j])
    return prod


# Aplicar fórmula
def formula(val, vector_x, tabla, n):
    suma = tabla[0][0]
    for i in range(1, n):
        suma = suma + (producto(val, i, vector_x) * tabla[0][i])
    return suma


# Resultados
cprint('{: ^80}'.format(" INTERPOLACIÓN PARABÓLICA PROGRESIVA "), 'blue', attrs=['bold'], end="\n")

# Ingreso de vectores X e Y
x = list(map(float, input('Ingrese valores de X:').split()))  # [0, 0.4, 0.75, 1.5, 2]
y = list(map(float, input('Ingrese valores de Y:').split()))  # [1, 1.63246, 1.86603, 2.22474, 2.41421]

# Valor a interpolar
valor = float(input('Valor a interpolar: '))  # 1

# Cantidad de términos a usar
cant_term = 4

# Tabla de Diferencias
tabla_dif = calcular_diferencias(y, x)

print('{: ^80}'.format('Tabla de Diferencias Divididas\n'))
imprimir(tabla_dif, x, y)
resultado = formula(valor, x, tabla_dif, cant_term)
print("\nF(x = " + str(valor) + "): {:g}".format(resultado))
