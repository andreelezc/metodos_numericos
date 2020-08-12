# Las medidas de tiempo de un recorrido efectuadas por diferentes alumnos son:
# 3,01 s; 3.11 s; 3,20 s; 3,15 s
# El valor que se considera exacto es: 3.12s
# Hallar los errores absoluto y relativo de cada medida

from prettytable import PrettyTable
from decimal import Decimal
from TP2.Errores import *

valores = [Decimal('3.01'), Decimal('3.11'), Decimal('3.20'), Decimal('3.15')]
p_real = Decimal('3.12')
e_rel = []
e_abs = []

for num in valores:
    e_abs.append(error_absoluto(4, p_real, num))
    e_rel.append(error_relativo(4, p_real, num))

t = PrettyTable()
t.add_column('Alumno', ['a', 'b', 'c', 'd'])
t.add_column('Tiempo', valores)
t.add_column('Error Absoluto', e_abs)
t.add_column('Error Relativo', e_rel)

print('Valor Exacto:', p_real)
print(t)
