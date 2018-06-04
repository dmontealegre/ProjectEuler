# we check how many primes satisfy p^2 < 10^8.
# any combination of two of them would work.
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

bound = 10**8
primes = primes2(bound)

count = 0

for x in range(len(primes)):
    pointer = x
    counter = 0
    if primes[x]**2 > bound:
        break
    while primes[x]*primes[pointer] < bound:
        pointer += 1
        counter += 1
    count += counter

print(count)
