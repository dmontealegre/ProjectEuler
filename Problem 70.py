from primes import *
import itertools
import collections
import time

start = time.time()
# TODO make the phi function computation faster. Takes 32 seconds to compute the phi function of numbers up to 10^6
bound = 10 ** 7

primes1 = primes2(bound)
primes = set(primes1)
print('done getting the primes')
phi = {}
for p in primes:
    k = 1
    while p ** k < bound:
        phi[p**k] = p**k - p ** (k-1)
        k += 1

print('done with computing phi of the primes')
def get_factors(n):
    for p in primes1:
        if n % p == 0:
            t = 1
            while n % (p ** t) == 0:
                t += 1
            t -= 1
            return p ** t, n // (p**t)

for n in range(2, bound):
    if n not in phi.keys():
        # for p in primes:
        #     if n % p == 0:
        #         n = int(n * ( 1 - 1 / p))
        #     if p > n:
        #         break
        a1, a2 = get_factors(n)
        phi[n] = phi[a1] * phi[a2]


print('done computing phi ', time.time() - start)

def are_permutations(a,b):
    a = str(a)
    b = str(b)
    count_a = collections.Counter()
    count_b = collections.Counter()
    for char in a:
        count_a[char] += 1
    for char in b:
        count_b[char] += 1
    return count_a == count_b

minimum = bound
for n in range(2,bound):
    if n % (10 ** 6) == 0:
        print('done with a n = ', n)
    if are_permutations(n, phi[n]) and n/phi[n] < minimum:
        print('best n so far is', n)
        minimum = n/phi[n]
