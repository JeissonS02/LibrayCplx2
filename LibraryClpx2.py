
import numpy as np


def suma_vect(vector1, vector2):
    max_length = max(len(vector1), len(vector2))
    vector1 = vector1 + [0j] * (max_length - len(vector1))
    vector2 = vector2 + [0j] * (max_length - len(vector2))

    result = [x + y for x, y in zip(vector1, vector2)]
    return result


def inverso_Adi(vector):

    inverso_vect = [-x for x in vector]

    return inverso_vect

def mult_escalar(escalar, vector):
    resultado = [escalar * x for x in vector]
    return resultado


def suma_mat_cplx(matriz1, matriz2):
    f1, c1 = len(matriz1), len(matriz1[0])
    f2, c2 = len(matriz2), len(matriz2[0])

    if f1 != f2 or c1 != c2:
        return None

    resultado = []
    for i in range(f1):
        row = []
        for j in range(f1):
            row.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(row)

    return resultado


def inversa_aditiva_cplx(matrix):
    f = len(matrix)
    c = len(matrix[0])

    matriz_inversa = [[0j] * c for _ in range(f)]

    for i in range(f):
        for j in range(c):
            matriz_inversa[i][j] = -matrix[i][j]

    return matriz_inversa

def mult_escalar_matriz(escalar, matriz):
    f = len(matriz)
    c = len(matriz[0])

    resultado = [[0j] * c for _ in range(f)]

    for i in range(f):
        for j in range(c):
            resultado[i][j] = escalar * matriz[i][j]

    return resultado


def trans_matriz(matriz):
    if not matriz:
        return []

    f = len(matriz)
    c = len(matriz[0])

    transpuesta = [[matriz[j][i] for j in range(f)] for i in range(c)]

    return transpuesta

def matriz_conjugada(matriz):
    matriz_c = []
    for f in matriz:
        fila_c = []
        for complejo in f:
            fila_c.append(complejo.conjugate())
        matriz_c.append(fila_c)
    return matriz_c



