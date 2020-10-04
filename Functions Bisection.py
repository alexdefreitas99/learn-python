from __future__ import division


# f(x) = x^3 – 9x + 3.
def funcao(x0): return x0 ** 3 - 9 * x0 + 3


# a = Extremo esquerdo do intervalo de inspeção [a,b]
# b = Extremo esquerdo do intervalo de inspeção [a,b]
# TOL = Tolerância (critério de parada).
# N = Número máximo de iterações.
def biss(a, b, TOL, N):
    f0 = funcao(a)
    i = 1
    while (abs(funcao(a)) > TOL) and (abs(funcao(b)) > TOL) and (i <= N):
        if abs(a - b) < TOL:
            media = (a + b) / 2
            f2 = funcao(media)
            if f0 * f2 < 0:
                b = media
                f1 = funcao(media)
            else:
                a = media
                f0 = funcao(media)
                i = i + i
            if i > N:
                print("Não houve convergência")
            if abs(funcao(a)) < TOL:
                raiz = a
            else:
                raiz = b
            return raiz

# Retorno = Aproximação da raiz.
