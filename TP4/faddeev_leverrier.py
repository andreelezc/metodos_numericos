import numpy as np
from numpy import linalg as la
from Utils.Impresion import matprint
from termcolor import cprint

a = np.array([[3, -2, 4, -2],
              [5, 3, -3, -2],
              [5, -2, 2, -2],
              [5, -2, -3, 3]])

eigvals, eigvec = la.eig(a)
eigvals = eigvals.real
eigvec = eigvec.real
pc = np.poly(a)

for i in range(len(eigvec)):
    eigvec[i] = np.around(eigvec[i], 2)
for i in range(len(eigvals)):
    eigvals[i] = np.around(eigvals[i], 2)


cprint('{: ^80}'.format(" FADDEEV LEVERRIER "), 'blue', attrs=['bold'], end="\n")
print('Matriz ingresada:')
matprint(a)

print('\nEigenvalores:\n', eigvals)
print('\nEigenvectores:\n')
matprint(eigvec)
print('\nPolinomio Característico:\n', np.poly1d(pc))

