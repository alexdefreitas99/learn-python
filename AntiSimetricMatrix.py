import numpy as np

# a = np.array([[3, -1, 4], [0, 3, 2], [0, 0, 3]])
# a = np.array([[3, -3], [3, -3], [3, -3]])
a = np.array([[0, -1, -4], [1, 0, 2], [4, -2, 0]])
# a = np.array([[3, -1, 4], [0, 3, 2], [0, 0, 3]])
# np.all
#
# def transpoeMatriz(a): return a.T;


def check_symmetric(a, tol=1e-8):
    return np.all(np.abs(a-a.T) < tol)

print(check_symmetric(a));