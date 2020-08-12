# Módulo para calcular error absoluto y relativo de un número.
# Ambas funciones reciben:
# n: cantidad de decimales deseados
# v_real: valor real de la solución
# v_aprox: valor aproximado


def error_absoluto(n, v_real, v_aprox):
    e_abs = abs(v_real - v_aprox)
    formato = '{:.' + str(n) + 'f}'
    return formato.format(e_abs)


def error_relativo(n, v_real, v_aprox):
    e_rel = abs((v_real - v_aprox)/v_real)
    formato = '{:.' + str(n) + 'f}'
    return formato.format(e_rel)
