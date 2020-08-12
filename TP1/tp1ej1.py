# Ejercicio Nº 1
# Modelo matemático: x1 + x2 + .. + xn-1 + xn

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

n = int(input('Ingrese número de términos:'))
x = []
suma = 0.0
for i in range(1, n+1):
    x.append(float(input('X' + str(i).translate(SUB) + ' = ')))
suma = sum(x)
print('Resultado Final:', '{:.2f}'.format(suma))
