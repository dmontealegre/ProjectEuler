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

print(sum(sieve(2000000)))