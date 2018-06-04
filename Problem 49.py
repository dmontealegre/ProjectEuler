import itertools

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

list_of_primes = primes2(10000)

filtered_primes = [list_of_primes[i] for i in range(len(list_of_primes)) if len(str(list_of_primes[i])) == 4]

orbits = []

for element in filtered_primes:
    orbit = []
    for i in itertools.permutations(str(element)):
        string = ''
        for j in range(len(i)):
            string += i[j]
        if int(string) in filtered_primes:
            orbit.append(int(string))
    if len(list(set(orbit)))>= 3:
        orbits.append(list(set(orbit)))

def check_as(tuple):
    if tuple[1] - tuple[0] == tuple[2]-tuple[1]:
        return True

answer = []

for i in orbits:
    for j in itertools.permutations(i, 3):
        if check_as(j):
            answer.append(set(j))


print(list(set(frozenset(item) for item in answer)))



