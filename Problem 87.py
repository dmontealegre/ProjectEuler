from primes import *
import math


bound = 50

primes = primes2(int(math.sqrt(bound)))
results = []
for p1 in primes:
    for p2 in primes:
        if p2 ** 3 > bound:
            break
        for p3 in primes:
            if p3 ** 4 > bound:
                break
            else:
                temp = p1** 2 + p2 ** 3 + p3 ** 4
                if temp < bound:
                    results.append(temp)

print(len(set(results)))
