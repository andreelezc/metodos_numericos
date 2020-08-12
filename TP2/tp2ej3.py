# Supóngase que se tiene que medir la longitud de un puente (x) y la de un remache (y),
# obteniéndose 9.999 y 9 cm respectivamente. Si los valores verdaderos son 10.000 y 10, calcular:
# a) El error absoluto verdadero
# b) El error relativo verdadero

from TP2.Errores import *
from decimal import Decimal, getcontext

getcontext()

x = Decimal(9999)
x_v = Decimal(10000)

y = Decimal(9)
y_v = Decimal(10)

print('x) Error absoluto:', error_absoluto(2, x, x_v), '\tError Relativo:', error_relativo(6, x, x_v))
print('Y) Error absoluto:', error_absoluto(2, y, y_v), '\tError Relativo:', error_relativo(6, y, y_v))
