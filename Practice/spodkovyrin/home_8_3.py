import itertools


def chain(lst1, lst2, lst3):
    return list(itertools.chain(lst1, lst2, lst3))

def filter_false(a):
    return list(itertools.filterfalse(lambda x: len(x) < 5, a))

def combinations(s):
    return list(itertools.combinations(s, 4))

print(chain([1, 2, 3], [4, 5], [6, 7]))
print(filter_false(['hello', 'i', 'write', 'cool', 'code']))
print(*combinations('password'), sep='\n')
