from itertools import permutations,tee
import funcionalities
import values

def rSubset(arr :list, r : int):
    return list(permutations(arr, r))
  
grafo = rSubset('ABCDE', 5)

possibilidades = 0
possibilidades_totais = 0
for i in grafo:
    soma=0
    
    for separetedValues in funcionalities.getSeparetedValues(list(i)):
        soma += values.verifyValues(list(separetedValues))

    if soma <= 19:
        possibilidades += 1
        print(f'sequencia vertices: {i},  Soma arestas: {soma} Km')

    possibilidades_totais +=1
    soma = 0
print(f"Possibilidades abaixo de 19: {possibilidades}")
print(f"Possibilidade totais: {possibilidades_totais}")