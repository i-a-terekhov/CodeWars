import itertools

def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))
