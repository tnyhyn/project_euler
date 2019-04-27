import itertools


def lp(n):
    x = itertools.permutations(range(10))
    counter = 1
    for i in x:
        if counter == n: return i
        counter += 1
    

print(lp(1000000))
