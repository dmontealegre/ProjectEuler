import time

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
    return [2, 3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

primes = primes2(1000000)

def is_truncable(n):
    string = str(n)
    for i in range(len(string)-1):
        string = string[1:]
        if int(string) not in primes:
            return False
    string = str(n)
    for i in range(len(string)-1):
        string = string[:-1]
        if int(string) not in primes:
            return False
    return True

count = 0
summation = 0
filtered_primes = [i for i in primes if (int(str(i)[0]) or int(str(i)[-1])) not in [1, 4, 6, 8, 9]]

for i in filtered_primes:
    if i > 7 and is_truncable(i):
        count += 1
        summation += i
        if count == 11:
            break

print(summation)

timer = time.time() - start
print('took %s seconds' % timer)
