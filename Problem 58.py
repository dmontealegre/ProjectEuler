import math

# TODO improve the speed. Takes a few minutes to run. 

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


primes = set(primes2(1000000000))
print('primes loaded')

diag = [1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49]
diag_primes = [3, 5, 7, 13, 17, 31, 37, 43]
pointer = 49
n = 4

# side is of length (2n-1)^2

while True:
    if len(diag_primes)/len(diag) < .10:
        print(diag[-1])
        print(math.sqrt(diag[-1]))
        break
    else:
        for _ in range(4):
            diag.append(pointer + 2*n)
            if pointer + 2*n in primes:
                diag_primes.append(pointer + 2*n)
            pointer += 2*n
        # print('diagonals = ', diag)
        # print('primes in diag = ', diag_primes)
        # print(len(diag_primes)/len(diag))
        n += 1


