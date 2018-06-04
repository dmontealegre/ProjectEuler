import math
def passes_goldbach(n, P):
        for i in range(0,len(P)):
            if (n-P[i])%2 == 0:
                if is_square((n-P[i])/2)== True:
                    print(n, '=',P[i],'+2*', math.sqrt((n-P[i])/2))
                    return True



def is_square(apositiveint):
    if apositiveint ==0:
        return False
    if apositiveint ==1:
        return True
    x = apositiveint // 2
    seen = set([x])
    if x == 0:
        return False
    else:
        while x * x != apositiveint:
            x = (x + (apositiveint // x)) // 2
            if x in seen: return False
            seen.add(x)
        return True



def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes



def passes_goldbach2(n,P):
    for i in range(0,len(P)):
        if n-P[i] % 2 == 0:
            print(n-P[i])

def function(n, P):
    for i in range(0,len(P)):
        if (n-P[i])%2 == 0:
            if is_square((n-P[i])/2)==True:
                return True
    else:
        return False




#P= primes_sieve(5000)
#for x in range(1,3000):
#    if function(2*x+1,P)==False:
#        print(2*x+1)
