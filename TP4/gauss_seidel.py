import numpy as np
from termcolor import cprint
from Utils.Impresion import matprint


def gauss_seidel(matriz, x0=None, eps=1e-5, max_iter=100):
    """
    Parametros
    ----------
    matriz  : matriz de coeficientes
    x0 : valores iniciales de las incognitas
    eps: tolerancia del error
    max_iter: numero máximo de iteraciones

    Retorna
    -------
        Arreglo con la solución del sistema | None

    """

    np.asarray(matriz)
    n, m = matriz.shape

    if n == m:
        return None

    x0 = [0] * (m - 1) if x0 is None else x0
    x1 = x0[:]
    k = 0
    while k <= max_iter:
        k = k + 1
        for i in range(0, n):
            suma = 0
            for j in range(0, m - 1):
                if j != i:
                    suma = suma + matriz[i, j] * x1[j]
            x1[i] = (matriz[i][m-1] - suma) / matriz[i, i]

        if all(abs(x1[i] - x0[i]) < eps for i in range(m - 1)):
            return x1
        x0 = x1[:]
    return None


a = np.array([[10, 1, 2, 44],
              [2, 10, 1, 51],
              [1, 2, 10, 61]])

# a = np.array([[3.0, -0.1, -0.2, 7.85],
#               [0.1, 7.0, -0.3, -19.30],
#               [0.3, -0.2, -10.3, -19.30]])

# a = np.array([[3, -2, 4, -2],
#               [5, 3, -3, -2],
#               [5, -2, 2, -2],
#               [5, -2, -3, 3]])


cprint('{: ^80}'.format(" GAUSS SEIDEL "), 'blue', attrs=['bold'], end="\n")
print('Matriz [A | b]:')
matprint(a)

resultado = gauss_seidel(a)
if resultado is not None:
    print('\nResultados:')
    for r in range(1, len(resultado)+1):
        print('x' + str(r) + ' = ' + str(np.around(resultado[r-1], 2)))
else:
    print('\nLa solución no converge.')
