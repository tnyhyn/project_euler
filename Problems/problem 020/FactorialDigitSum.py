def solve(x):
    bignumber = list(str(factorial(x)))
    acc = 0
    for i in bignumber:
        acc = acc + int(i)
    print(acc)

def factorial(x):
    if x == 1: return 1
    else: return x * factorial(x-1)
        
solve(100)