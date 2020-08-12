# Calcule el error absoluto y relativo en las siguientes aproximaciones de p por p*
# a) P = π , p* = 22/7 
# b) p = π , p*= 3.1416

from decimal import Decimal, getcontext
from TP2.Errores import *
import math

getcontext()


p_real = Decimal(math.pi)
p_aprox_a = Decimal(22)/Decimal(7)
p_aprox_b = Decimal(3.1416)

print('a) Error absoluto:', error_absoluto(6, p_real, p_aprox_a), '\tError Relativo:', error_relativo(6, p_real, p_aprox_a))
print('b) Error absoluto:', error_absoluto(6, p_real, p_aprox_b), '\tError Relativo:', error_relativo(6, p_real, p_aprox_b))

