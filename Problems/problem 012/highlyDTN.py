import math


def divisors(n):
    divList = []
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            divList.append(i)
        i += 1
    divSet = set(divList)
    for i in divList:
        divSet.add(n/i)
    return len(divSet)


def dtn():
    triFor = lambda a : a * (a + 1) / 2
    i = 1000
    while True:
        if divisors(triFor(i)) >= 500:
            return triFor(i)
        i += 1


print(dtn())
