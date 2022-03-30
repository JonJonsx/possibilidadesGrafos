from itertools import product,tee

values = {
    "AA": 0,
    "BB": 0,
    "CC": 0,
    "DD": 0,
    "EE": 0,
    "AB": 1,
    "BA": 1,
    "BC": 2,
    "CB": 2,
    "CD": 3,
    "DC": 3,
    "DE": 4,
    "ED": 4,
    "EA": 5,
    "AE": 5,
    "AC": 6,
    "CA": 6,
    "CE": 7,
    "EC": 7,
    "BE": 8,
    "EB": 8,
    "BD": 9,
    "DB": 9,
    "AD": 10,
    "DA": 10
}


def verifyValues(value:list):
    alter_value = "".join(str(x) for x in value)
    for i in values:
        if alter_value == i:
            return values[i]

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

