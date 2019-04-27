import math


def amicable(x):
    amicable = []
    for i in range(0, 10001):
        divSum = divisors(i)
        if divSum == i: continue
        if divisors(divSum) == i:
            amicable.append(i)
    print(amicable)
    return sum(amicable)

def divisors(n):
    divList = []
    i = 1
    while i <= n/2:
        if n % i == 0:
            divList.append(i)
        i += 1
    return sum(divList)

print(amicable(10000))
## 31626