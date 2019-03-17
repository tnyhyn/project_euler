# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n%i == 0:
            return False
    return True

def solve():
    sum = 0
    for i in range(2, 2000001):
        if isPrime(i):
            sum += i
    print(sum)

solve()

# Answer: 142913828922