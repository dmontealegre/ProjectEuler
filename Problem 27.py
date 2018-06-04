# observation 1: b must be a positive prime (b.c. when we plug in n=0 we must have a prime)

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2, 3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

# we get the primes up to 10^6. Make it a set for easy look up.
primes = set(primes2(1000000))
possible_b = primes2(1000)


def length(a, b):
    n = 0
    while True:
        if n**2 + a*n + b not in primes:
            return n
            break
        n += 1

best = 0

# check that a must be odd.
for a in range(-1000, 1001):
    for b in possible_b:
        if length(a, b) > best:
            best = length(a, b)
            print(a, b, best)
