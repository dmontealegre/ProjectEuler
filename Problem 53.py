import math

def choose(n,r):
    return int(math.factorial(n) / math.factorial(r) / math.factorial(n-r))


summation = 0


for n in range(23,101):
    for r in range(0, n):
        while True:
            if choose(n, r) > 1000000:
                summation += (n + 1 - 2*r)
                break
            r += 1
        break

print(summation)


