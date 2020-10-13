import numpy as np


def metodoRetroativo(matrizCoeficientes, termosIndependnetes):
    x = np.zeros(3)
    x[2] = b[2] / A[2][2]
    for i in np.arange(1, -1, -1):
        SOMA = 0
        for j in np.arange(i + 1, 3):
            SOMA = SOMA + A[i][j] * x[j]
        x[i] = (b[i] - SOMA) / A[i][i]
    print('Método retroativo: ', x)
    return x


def fatoraLU(A):
    U = np.copy(A)
    n = np.shape(U)[0]
    L = np.eye(n)
    for j in np.arange(n - 1):
        for i in np.arange(j + 1, n):
            L[i, j] = U[i, j] / U[j, j]
            for k in np.arange(j + 1, n):
                U[i, k] = U[i, k] - L[i, j] * U[j, k]
                U[i, j] = 0
    print('Matriz L: ', L)
    print('Matriz U: ', U)
    return L, U


# A = np.array([[1, 1, 1], [0, 1, -3], [0, 0, -13]])  # Matriz dos coeficientes
# b = ([7, -10, -52])  # Termos independentes

A = np.array([[2, 3, 1], [0, 3, 0], [0, 0, 3.5]])
b = ([2, -3, 3.5])
metodoRetroativo(A, b)

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
fatoraLU(A)
