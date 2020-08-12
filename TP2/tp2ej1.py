# Se realizaron mediciones de la base y la altura de un rectángulo. Los valores
# obtenidos fueron: base a = 5.3 cm y altura b = 2.4 cm. Calcular el perímetro y el
# área del rectángulo teniendo en cuenta que la altura fue medida con un error +/ 0.1
# cm. y la base con un error +/ 0.2 cm. Obtener conclusiones.

from decimal import Decimal, getcontext

getcontext().prec = 4

base = Decimal(5.3)
altura = Decimal(2.4)

p_max = Decimal(2 * (base + Decimal(0.1))) + Decimal(2 * (altura + Decimal(0.2)))
p_min = Decimal(2 * (base - Decimal(0.1))) + Decimal(2 * (altura - Decimal(0.2)))
p_medio = Decimal(p_max + p_min) / Decimal(2)

e_abs_max = abs(p_max - p_medio)
e_abs_min = abs(p_min - p_medio)

e_rel = Decimal(e_abs_max / p_medio)

print('Error Absoluto Maximo:', e_abs_max)
print('Error Absoluto Mínimo:', e_abs_min)
print('Error Relativo:', e_rel)
