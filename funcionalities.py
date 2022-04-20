from itertools import tee

def pairwise(iterable):
# pairwise('ABCDE') --> AB BC CD DE
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)  

def getSeparetedValues(values: list):
    return list(pairwise(values))