
def sieve(limit):
    a = [True]*limit
    for i in range(2, limit):
        if a[i]:
            for j in range(i*i, limit, i):
                a[j] = False
    primes = []
    for i in range(2,limit):
        if a[i]:
            primes.append(i)
    return primes

def is_pandigital(number):
    string = str(number)
    length = len(string)
    digits = {str(i) for i in range(1, length+1)}
    return digits == set(string)

# since we are looking for a pandigital prime, then we know it must have 7 digits at most. 8, 9 pandigital numbers
# are divisible by 3.
primes = sieve(7654321)


for i in range(len(primes)-1, 2, -1):
    if is_pandigital(primes[i]):
        print(primes[i])
        break


