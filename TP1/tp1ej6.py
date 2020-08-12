# Ejercicio Nº6
# Modelo matemático: ∑(i=0..n) 1/N!

import math


def factorial(n):
    fact = 1
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(1, n + 1):
            fact = fact * i
        return fact


def main():
    n = int(input('Número de términos:'))
    e = 0
    print('e = ', end='')
    for i in range(n+1):
        if i != n:
            print('1/', i, '! + ', end='')
        else:
            print('1/', i, '!', end='')
        e = e + (1/factorial(i))
    print('\ne =', '{:.2f}'.format(e))


# Alternativa usando función nativa
# def main():
#     n = int(input('Número de términos:'))
#     e = 0
#     for i in range(1, n + 1):
#         e = e + (1 / math.factorial(i))
#     print('e = ', '{:.2f}'.format(e))


main()
