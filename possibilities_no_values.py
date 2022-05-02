from itertools import product

import funcionalities


def rSubset(arr: list, r: int):
    return list(product(arr, repeat=r))


def possibilities_no_values(vertices, valor):
    grafo = rSubset(vertices, valor)
    vertices = []
    for i in grafo:
        valores = []
        for separatedValues in funcionalities.getSeparetedValues(list(i)):
            if separatedValues[0] == separatedValues[1]:
                valores.append(0)

        if 0 not in valores:
            vertices.append(i)
        valores = []

    print(vertices)
    print(len(vertices))
