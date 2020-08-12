# Ejercicio Nº4
# Modelo matemático: saldo = balance + depósito - retiro

from prettytable import PrettyTable

tabla = [['06/07', 220.13, 327.26, 0],
         ['07/07', 216.8, 378.62, 0],
         ['08/07', 320.25, 106.8, 0]]

balance_ant = 512.33

t = PrettyTable()
t.field_names = ['Fecha', 'Depósito', 'Retiro', 'Balance']
t.add_row(['05/07', '-', '-', 512.33])

for fila in tabla:
    fila[3] = round(balance_ant + fila[1] - fila[2], 2)
    balance_ant = fila[3]
    t.add_row(fila)

print(t)
print('Saldo Final:', balance_ant)
