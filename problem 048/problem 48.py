#Problem 48
#Self Powers

import time

start_time = time.time()

def power(base, exp):
    sum = 1
    for x in range(0,exp):
        sum = sum * base
    return sum

def selfPowers(base, exp):
    sum = 0
    while (exp > 0):
        sum = sum + power(base,exp)
        base = base - 1
        exp = exp - 1
    return sum    

sum = selfPowers(1000,1000)

print(sum)
print("exec time is %s seconds" % (time.time() - start_time))
