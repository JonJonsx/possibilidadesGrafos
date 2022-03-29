from itertools import product,tee

def verifyValues(value: list):
    if value == ['A', 'A'] or value == ['B', 'B'] or value == ['C', 'C'] or value == ['D', 'D'] or value == ['E', 'E']:
        return 0
    elif value == ['A', 'B'] or value == ['B', 'A']:
        return 1
    elif value == ['B','C'] or value == ['C','B']:
        return 2
    elif value == ['C','D'] or value == ['D','C']:
        return 3
    elif value == ['D','E'] or value == ['E','D']:
        return 4
    elif value == ['E','A'] or value == ['A','E']:
        return 5
    elif value == ['A','C'] or value == ['C','A']:
        return 6
    elif value == ['C','E'] or value == ['E','C']:
        return 7
    elif value == ['B','E'] or value == ['E','B']:
        return 8
    elif value == ['B','D'] or value == ['D','B']:
        return 9
    elif value == ['A','D'] or value == ['D','A']:
        return 10

def pairwise(iterable):
    # pairwise('ABCDE') --> AB BC CD DE
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)  

def getSeparetedValues(values: list):
    return list(pairwise(values))

def rSubset(arr :list, r : int):
    return list(product(arr, repeat=r))

vertices = rSubset('ABCDE', 5)
newVertices = []


possibilidades = 0 
copyVertices = vertices
for i in vertices:
    soma=0
    
    for separetedValues in getSeparetedValues(list(i)):
        soma += verifyValues(list(separetedValues))
        if soma == 0:
            copyVertices.remove(i)


    if soma <= 19:
        possibilidades += 1
        # print(f'sequencia vertices: {i},  Soma arestas: {soma} Km')

    soma = 0


print(f"copyVertices: {copyVertices}")
print(f"vertices: {vertices}")
print("Possibilidades: ",possibilidades)

