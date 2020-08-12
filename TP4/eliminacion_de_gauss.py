import numpy as np
from termcolor import cprint
from sympy import *

# La matriz ingresada debe ser de la forma [A|b] donde A son los coeficientes y b los resultados.


def gauss(matriz):
    np.asarray(matriz)  # Asegura que la matriz ingresada sea tipo array
    matriz = matriz.astype(float)  # Tipo de datos float
    print('Matriz Inicial:')
    print(matriz)

    if matriz[0, 0] == 0.0:
        raise Exception('\nEl elemento [1,1] no puede ser cero')

    n, m = matriz.shape

    # Eliminación de Incógnitas
    for i in range(0, n):  # fila
        for j in range(i + 1, n):
            if matriz[j, i] != 0.0:
                print('\nFila Pivote:', i, 'Fila resultado:', j)
                multiplicador = matriz[j, i] / matriz[i, i]
                matriz[j, i:m] = matriz[j, i:m] - multiplicador * matriz[i, i:m]
                print(matriz)

    # Sustitución hacia atrás
    x = []
    subs = 0.0
    for i in range(n - 1, -1, -1):  # fila
        for j in range(0, n - i):  # columna
            if j == 0:
                subs = 0
            else:
                subs = subs + matriz[i, m - j - 1] * x[j - 1]
        x.append((matriz[i, m - 1] - subs) / matriz[i, i])
    return x[::-1]


a = np.array([[4, 8, 4, 80],
              [2, 1, -4, 7],
              [3, -1, 2, 22]]
             )

cprint('{: ^100}'.format(" ELIMINACIÓN DE GAUSS "), 'blue', attrs=['bold'], end="\n")
resultado = gauss(a)
print('\nResultados:')
for r in range(1, len(resultado)+1):
    print('X' + str(r) + ' = ', resultado[r-1])

# a = Matrix([[4, 8, 4, 80],
#             [2, 1, -4, 7],
#             [3, -1, 2, 22]])
#
# pretty_print(a.echelon_form())
