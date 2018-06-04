# use phi(n) = n prod_{p | n} (1 - 1/p) gives us a short solution:

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

primes = primes2(1000000)

number = 1
x = 0

while number < 1000000:
    print(number)
    number *= primes[x]
    x += 1


print(number // primes[x-1])