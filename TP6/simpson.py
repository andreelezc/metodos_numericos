def simpson(vector_x, vector_y):
    n = len(vector_y)

    # Verifica si la cantidad de puntos es par
    if n % 2 == 0:
        return 'No se puede aplicar la fórmula de Simpson.'
    else:
        h = vector_x[1] - vector_x[0]
        e = vector_y[0] + vector_y[-1]
        pares = round(sum(vector_y[2:n-1:2]), 5)
        impares = round(sum(vector_y[1:n-1:2]), 5)
        area = (h/3) * (e + (2 * pares) + (4 * impares))

        aux = 'E = ' + str(e) + '\nP = ' + str(pares) + '\nI = ' + str(impares)
        return aux + '\nÁrea ≅ {:g}'.format(area)


def simpson3(vx, vy):
    n = len(vy)

    # Verifica que la cantidad de puntos sea impar
    if n % 2 != 0:
        return 'No se puede aplicar la fórmula de 3/8 Simpson.'
    else:
        h = vx[1] - vx[0]
        area = (3/8 * h) * (vy[0] + (3 * vy[1]) + (3 * vy[2]) + vy[3])
        return 'Área ≅ {:g}'.format(area)
