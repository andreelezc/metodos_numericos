from sympy import *
from termcolor import cprint

A = Matrix([[25, 5, 1, 106.8],
           [64, 8, 1, 177.2],
           [144, 12, 1, 179.2]])

cprint('{: ^100}'.format(" GAUSS JORDAN "), 'blue', attrs=['bold'], end="\n")
print('Matriz ingresada:\n')
pretty_print(A)
print('\nResultado:\n')
pretty_print(A.rref())
