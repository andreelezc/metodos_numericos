# Ejercicio Nº 7
# Modelo matemático PI = 4 * Σ (-1)^n / 2n+1; n=0 - ∞

import math
from decimal import getcontext, Decimal

n = int(input('Cantidad de decimales:'))
getcontext().prec = n + 1

r = Decimal(0)
mod = Decimal(1) / Decimal(10) ** Decimal(n)

pi = Decimal(math.pi) - Decimal(math.pi) % mod
pi_aprox = Decimal(0)

print('PI = 4 * (', end=' ')
while pi != pi_aprox - pi_aprox % mod:
    pi_aprox += Decimal(4) / Decimal(2 * r + 1) * Decimal((-1) ** r)
    if 2*r+1 == 1:
        print('1', end=' ')
    elif (-1)**r < 0:
        print(' - 1/', 2*r+1, end=' ')
    else:
        print(' + 1/',  2*r+1, end=' ')
    r += 1
print(')')

print('\nSon necesarios', r, 'términos')
print('Pi Real:', math.pi)
print('Valor aproximado:', pi_aprox)
