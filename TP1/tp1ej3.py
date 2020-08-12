# Ejercicio Nº 3
# Modelo matemático: (-b ±  √(b^2 - 4*a*c)) / 2*a

import math

a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))

disc = (b**2)-(4*a*c)

if disc < 0:
    disc = disc * (-1)
    raiz_real = (0-b)/(2*a)
    raiz_img = math.sqrt(disc) / (2*a)
    print('X1 = ', '{:.2f}'.format(raiz_real), ' + ', '{:.2f}'.format(raiz_img), 'i')
    print('X2 = ', '{:.2f}'.format(raiz_real), ' - ', '{:.2f}'.format(raiz_img), 'i')
else:
    x1 = ((0-b) + (math.sqrt(disc)) / (2*a))
    x2 = ((0-b) - (math.sqrt(disc)) / (2*a))
    print('X1 = ', '{:.2f}'.format(x1))
    print('X1 = ', '{:.2f}'.format(x2))

