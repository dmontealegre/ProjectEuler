import time

# TODO this program first calculates the primes up to a value, which is slow.
start = time.time()

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]


list_primes = primes2(200000)

prime_factors = {}
n = 200000

for i in range(n):
    if i in list_primes:
        prime_factors[i] = [i]
    else:
        for j in range(2, i//2 + 1):
            if i % j == 0:
                prime_factors[i] = list(set(prime_factors[i // j] + [j]))
                break

print('primes loaded')

counter = 0
pointer = 2
while True:
    if counter >= 4:
        # prints the last number of the sequence.
        print(pointer-1)
        break
    else:

        if len(prime_factors[pointer]) == 4:
            counter += 1
        else:
            counter = 0
        temp = prime_factors[pointer]
        pointer += 1
total_time = time.time()-start
print('solution took %s seconds' % total_time)
