import itertools


def permutations(s):
    rezult = []
    perm = set(itertools.permutations(s))
    for i in perm:
        element = ''
        for j in i:
            element += str(j)
        rezult.append(element)
    return rezult
