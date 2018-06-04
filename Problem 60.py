from primes import *
import itertools

n = 100000000
primes = primes2(n)
primes2test = [i for i in primes if i % 3 == 1] + [3]
primes = set(primes)

# going on a limp here. I think we must have 3 and 7 in our set.
x = 3
newset3 = []
for y in primes2test:
    if int(str(x)+str(y)) in primes and int(str(y)+str(x)) in primes:
        newset3.append(y)

newset3 = set(newset3)
x = 7
newset7 = []

for y in primes2test:
    if int(str(x)+str(y)) in primes and int(str(y)+str(x)) in primes:
        newset7.append(y)
newset7 = set(newset7)

pool = newset3.intersection(newset7)
print(len(pool))

# for subset in itertools.combinations(pool, 3):
#     answer = True
#     for pair in itertools.combinations(subset, 2):
#         if int(str(pair[0])+str(pair[1])) not in primes or int(str(pair[0])+str(pair[1])) not in primes:
#             answer = answer and False
#     if answer:
#         print(subset)
#
