from prettytable import PrettyTable
from termcolor import cprint


def lagrange(vector_x, vector_y, xo):
    pn_x = 0
    n = len(vector_x)
    for i in range(n):
        # Calculo de cada termino
        term = vector_y[i]
        for j in range(n):
            if j != i:
                term = term * (xo - vector_x[j]) / (vector_x[i] - vector_x[j])

        # Añadir termino al resultado general
        pn_x = pn_x + term
    return pn_x


def mostrar_tabla(vector_x, vector_y):
    t = PrettyTable()
    t.add_column('X', vector_x)
    t.add_column('Y', vector_y)
    print(t)


# Resultados
cprint('{: ^80}'.format(" INTERPOLACIÓN DE LAGRANGE "), 'blue', attrs=['bold'], end="\n")

# Ingreso de vectores X e Y
x = list(map(float, input('Ingrese valores de X:').split()))  # [0, 0.4, 0.75, 1.5, 2]; [102, 245, 327, 423, 565]
y = list(map(float, input('Ingrese valores de Y:').split()))  # [1, 1.63246, 1.86603, 2.22474, 2.41421]; [0.564642, 0.644218, 0.717356, 0.783327, 0.853329]

# Valor a interpolar
valor = float(input('Valor a interpolar: '))  # 1; 275

mostrar_tabla(x, y)
resultado = lagrange(x, y, valor)
print('Pn(' + str(valor) + ') = ' + '{:g}'.format(resultado))
