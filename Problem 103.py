import itertools


# given a1 and a2 we get an upper bound on a7.
def is_good(array):
    answer = True
    t1 = len(array)
    for i in range(1, t1+1):
        # pick a set B with i elements.
        for B in itertools.combinations(array,i):
            # now pick a set C disjoint from B:
            B = set(B)
            complement = set(array) - B
            t2 = t1 - i
            for j in range(1,t2+1):
                for C in itertools.combinations(complement, j):
                    if sum(C) == sum(B):
                        return False
                    if len(C) > len(B) and sum(C) <= sum(B):
                        return False
    return answer


# play around with different upper and lower bounds.
lower = 20
upper = 45
n = 7
best = upper*n
pool = [i for i in range(lower, upper+1)]

for array in itertools.combinations(pool,n):
    # since the combinations come in lexicographic order, we can stop looking once the bottom element is too large
    if array[0]*n > best:
        break
    array = list(array)
    if array[0]+array[1] < array[-1]:
        continue
    if sum(array) < best:
        if is_good(array):
            best = sum(array)
            print(array, best)

