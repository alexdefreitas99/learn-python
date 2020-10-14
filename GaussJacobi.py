from __future__ import division
import numpy as np
from numpy import linalg

matriz = np.array([
    [10, -1, 2, 0],
    [-5, 11, -1, 3],
    [3, -1, 10, -1],
    [1, 3, -1, 8]
])

termosIndependentes = np.array([6, 25, -11, 15])

estimativasIniciais = np.array([1, 1, 1, 1])

def jacobi(A, b, x0, tol, N):
    # preliminares
    A = A.astype('double')
    b = b.astype('double')
    x0 = x0.astype('double')

    n = np.shape(A)[0]
    x = np.zeros(n)
    it = 0
    iterations = 0
    # iteracoes
    while it < N:
        it = it + 1
        iterations = iterations + 1
        # iteracao de Jacobi
        for i in np.arange(n):
            x[i] = b[i]
            iterations = iterations + 1
            for j in np.concatenate((np.arange(0, i), np.arange(i + 1, n))):
                x[i] -= A[i, j] * x0[j]
                iterations = iterations + 1
            x[i] /= A[i, i]
            print(iterations)
            # tolerancia
        if np.linalg.norm(x - x0, np.inf) < tol:
            return x
            # prepara nova iteracao
        x0 = np.copy(x)
    raise NameError('num.max.de iteracoes excedido.')


print(jacobi(matriz, termosIndependentes, estimativasIniciais, 1, 10000))