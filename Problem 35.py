def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n // 3)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = [False] * ((n // 6 - k * k // 6 - 1) // k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = [False] * (
            (n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]


primes = primes2(1000000)


def is_circular(n):
    value = True
    string = str(n)
    for i in range(len(string)):
        string = string[1:] + string[0]
        value = value and int(string) in primes
        if not value:
            break
    return value


def is_good(number):
    string = str(number)
    for char in string:
        if char in {'0', '2', '4', '5', '6', '8'}:
            return False
    return True


a = [i for i in primes if is_good(i)]

# we start our summation at 2 because it eliminates 2 and 5 on the filtering but it is a circular prime trivially
summation = 2
for i in a:
    if is_circular(i):
        summation += 1

print(summation)
