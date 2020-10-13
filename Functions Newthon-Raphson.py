from __future__ import division


def derivada(x0): return 3 * x0 ** 2 - 9


# def funcao(x0): return x0 ** 3 - 9 * x0 + 3
def funcao(x0): return x0**4 - 3 * x0**3 + 3


def nr(x0, TOL, N):
    x1 = x0 - funcao(x0) / derivada(x0)
    i = 1
    while (abs(funcao(x1)) > TOL) and (i <= N):
        x0 = x1
        x1 = x0 - funcao(x0) / derivada(x0)
        i = i + i
        if i > N:
            print("Não houve convergência!")
        if abs(funcao(x1)) < TOL:
            return x1
