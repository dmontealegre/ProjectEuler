import time
# summation of euler's phi function.
# first we need the primes
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
    return [2, 3] + [3*i+1|1 for i in range(1, n//3-correction) if sieve[i]]


primes = primes2(100)
totient = {}
totient[1] = 1


def binary_search(array, number):
    if len(array) < 5:
        return number in array
    if number < array[0]:
        return False
    if number > array[-1]:
        return False
    else:
        index = len(array) // 2
        if array[index] > number:
            return binary_search(array[:index], number)
        else:
            return binary_search(array[index:], number)

for x in range(2, 100):
    key = x
    for p in primes:
            if x % p == 0:
                while x % p == 0:
                    x /= p
                totient[key] = int(totient[int(x)] * (1 - 1/p) * (key // x))
                break

summation = 0


# print(summation-1)

def sieve(limit):
    a = [[True, i] for i in range(limit)]
    for i in range(2, limit):
        if a[i][0]:
            for j in range(2*i, limit, i):
                a[j][0] = False
                a[j][1] = (a[j][1]* (1 - 1/i))
    for i in range(2,limit):
        if a[i][0]:
            a[i][1] -= 1
    return a

a = sieve(1000001)
for x in range(2, 1000001):
    summation += a[x][1]

print(a)
print(summation)