## Non-abundant sums
import math


def dSum(n):
    divList, i = [], 1
    while i <= math.sqrt(n):
        if n % i == 0:
            divList.append(i)
        i += 1
    divSet = set(divList)
    for i in divList:
        if i == 1: continue
        divSet.add(n/i)
    return sum(divSet)


def sumCheck(x, arr):
    for i in arr:
        if i > x: break
        for j in arr:
            if j > x: break
            if i + j == x: return False
    return True


def nas():
    nasList = []
    nasTwo = []
    for i in range(1, 28123):
        print(i)
        if dSum(i) > i: nasList.append(i)
    for j in range(1, 28123):
        if sumCheck(j, nasList): nasTwo.append(j)
        print(j)
    print(nasTwo)
    return sum(nasTwo)

print(nas())

## 4179871
## Takes like 10 minutes to run...lol...