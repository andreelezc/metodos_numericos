def trapecios(vector_x, vector_y):
    n = len(vector_y)

    # Longitud del intervalo
    h = vector_x[1] - vector_x[0]

    # Extremos
    e = vector_y[0] + vector_y[-1]

    # Calculo de elementos pares
    pares = round(sum(vector_y[2:n-1:2]), 5)

    # Calculo de elementos pares
    impares = round(sum(vector_y[1:n-1:2]), 5)

    # Aplicación de la formula
    area = h * ((e/2) + pares + impares)

    aux = 'E = ' + str(e) + '\nP = ' + str(pares) + '\nI = ' + str(impares)
    return aux + '\nÁrea ≅ {:g}'.format(area)
