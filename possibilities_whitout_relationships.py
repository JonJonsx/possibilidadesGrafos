from itertools import product,tee
import funcionalities
import values

def rSubset(arr :list, r : int):
    return list(product(arr, repeat=r))
    
grafo = rSubset("ABCDE", 5)

copyGrafo = []
for index,i in enumerate(grafo):
    soma=0
    result = []
    for separetedValues in funcionalities.getSeparetedValues(list(i)):
        result.append(values.verifyValues(list(separetedValues)))
    if 0 not in result:
        copyGrafo.append(i)
    result = []
    # if soma <= 19:

        # print(f'sequencia vertices: {i},  Soma arestas: {soma} Km')

print(f"copyVertices: {copyGrafo}")
# print(f"vertices: {vertices}")
print("Possibilidades: ",len(copyGrafo))

