# Ejercicio Nº5
# Modelo matemático:
#   Perimetro: 2*π*radio
#   Área: π*radio^2

import math

radio = float(input('Radio de la circunferencia:'))
perimetro = '{:.2f}'.format(2*math.pi*radio)
area = '{:.2f}'.format(math.pi*(radio**2))

print('Perímetro = ', perimetro, 'Área:', area)
