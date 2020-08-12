from TP6.simpson import *
from TP6.trapecios import *
from termcolor import cprint
from prettytable import PrettyTable

# x = [12, 13, 14, 15, 16, 17]
# y = [0.96262, 0.94718, 0.93108, 0.92221, 0.91181, 0.90151]

# x = [12, 13, 14, 15]
# y = [0.96262, 0.94718, 0.93108, 0.92221]

# x = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
# y = [0.0, 0.15, 0.3, 0.55, 0.73, 0.81]

# x = [0, 5, 10, 15, 20, 25, 30, 35, 40]
# y = [10, 22, 35, 47, 55, 58, 52, 40, 37]


def calcular_area(vector_x, vector_y):
    if len(vector_y) % 2 == 0:
        if len(vector_y) == 4:
            metodo = '3/8 Simpson'
            area = simpson3(vector_x, vector_y)
        else:
            metodo = 'Trapecios'
            area = trapecios(vector_x, vector_y)
    else:
        metodo = 'Simpson'
        area = simpson(vector_x, vector_y)
    print('Método a utilizar: {}'.format(metodo))
    return area


def imprimir(vx, vy):
    t = PrettyTable()
    t.add_column('X', 'Y')
    for i in range(len(vy)):
        t.add_column(str(vx[i]), [vy[i]])
    print(t)


# Resultados
cprint('{: ^80}'.format(" CÁLCULO DE ÁREA "), 'blue', attrs=['bold'], end="\n")

# Ingreso de vectores X e Y
x = list(map(float, input('Ingrese valores de X:').split()))
y = list(map(float, input('Ingrese valores de Y:').split()))

# Imprimir tabla
imprimir(x, y)

print('\nÁrea a integrar: [' + str(x[0]) + ', ' + str(x[-1]) + ']')
resultado = calcular_area(x, y)
print(resultado)
