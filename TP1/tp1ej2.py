# Ejercicio Nº2
# Modelo matemático: F = P(1 + i)^n

p = float(input('Cantidad de dinero P:'))
i = float(input('Tasa de interés:'))
n = int(input('Cantidad de periodos:'))
f = 0.0

print('Valor inicial: $', p, 'Tasa de interes:', i, 'Periodos:', n)

for j in range(1, n+1):
    f = (p * (1+i)) ** j
    print('Año:', j, 'Rendimiento:', '{:.2f}'.format(f))

